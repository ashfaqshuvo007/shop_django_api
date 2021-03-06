"""
    Created by tareq on ২৪/৬/১৯
"""
from datetime import datetime
from uuid import uuid4

from django.db import transaction
from django.db.models import ForeignKey, CASCADE, CharField, SmallIntegerField, DateTimeField
from django.urls import reverse

from configs.email_config import SYSTEM_FROM_EMAIL
from settings import SITE_ROOT
from sol_factory.base.models.domain_entity import DomainEntity
from sol_factory.base.utils.exceptions.system_error import SolFactorySystemError
from sol_factory.base.utils.tools.email_sender import EmailSender
from sol_factory.base.utils.tools.email_templates import get_user_verification_email_content
from sol_factory.users.enums.verification_status_enum import VerificationStatusEnum
from sol_factory.users.utils.exceptions.email_address_exception import UserDoesNotHaveEmailAddressException

__author__ = "Tareq"


class UserVerificationLink(DomainEntity):
    user = ForeignKey('users.ConsoleUser', on_delete=CASCADE)
    verification_uid = CharField(max_length=128)
    verification_status = SmallIntegerField(default=VerificationStatusEnum.Unverified.value)
    verified_time = DateTimeField(null=True)
    verification_sent_time = DateTimeField(null=True)

    class Meta:
        app_label = 'users'

    @classmethod
    def prepare_verification_link_for_user(cls, user):
        """
        This method prepares a verification link for a user
        :param user: a user instance
        :return: a newly created verification link
        """
        verification_link = cls(
            user=user, verification_uid=uuid4()
        )
        verification_link.save()
        return verification_link

    @classmethod
    def send_verification_link_to_user(cls, user, verification_link):
        """
        This method is used for sending an email to user containing verification link
        :param user: a user instance
        :return: boolean, True or False based on successfully sent email status
        """
        if not user.email:
            raise UserDoesNotHaveEmailAddressException(
                "User {} {} ({}) does not have an email address.".format(
                    user.first_name, user.last_name, user.username))
        email_content = get_user_verification_email_content(name=user.first_name, verification_link=SITE_ROOT + reverse(
            'user_verification_view', kwargs={'verification_code': str(verification_link.verification_uid)}))
        EmailSender.send_multipart_email(
            subject="Verify your Sol-Factory account", from_email=SYSTEM_FROM_EMAIL, to_email_list=[user.email],
            cc_list=[], bcc_list=[], text_content=email_content, html_content='')

        return False

    @classmethod
    def verify_user_via_verification_link(cls, verification_uid):
        """
        This method is used for verifying user when verification link is clicked.
        :param verification_uid: the uuid of verification link
        :return: the verified user instance
        """
        user_verification_link = cls.objects.filter(verification_uid=verification_uid).first()
        if not user_verification_link:
            raise SolFactorySystemError("User verification link with uid {} does not exist.".format(verification_uid, ))
        if user_verification_link.verification_status == VerificationStatusEnum.Verified.value:
            raise SolFactorySystemError(
                "User verification link with uid {} is already verified".format(verification_uid, ))

        with transaction.atomic():
            # verify the user
            user = user_verification_link.user
            user.verification_status = VerificationStatusEnum.Verified.value
            user.save()

            user_verification_link.verification_status = VerificationStatusEnum.Verified.value
            user_verification_link.verified_time = datetime.now()
            user_verification_link.save()

            return user
