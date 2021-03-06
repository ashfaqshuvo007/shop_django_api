"""
    Created by tareq on ২৬/৬/১৯
"""
from django.db.models import CharField, TextField, IntegerField

from sol_factory.base.models.domain_entity import DomainEntity

__author__ = "Tareq"


class EmailSendLog(DomainEntity):
    from_email_address = CharField(max_length=250)
    to_email_address_list = CharField(max_length=500, blank=True)
    cc_list = CharField(max_length=500, blank=True)
    bcc_list = CharField(max_length=500, blank=True)
    subject = CharField(max_length=500, blank=True)
    text_content = TextField(blank=True)
    html_content = TextField(blank=True)
    email_send_status = IntegerField(null=True)

    class Meta:
        app_label = 'logs'
