"""
    Created by tareq on ২৬/৬/১৯
"""
from django.core.mail import EmailMultiAlternatives

from sol_factory.logs.models.email_send_log import EmailSendLog

__author__ = "Tareq"


class EmailSender(object):
    @classmethod
    def send_multipart_email(cls, subject, from_email, to_email_list, cc_list, bcc_list, text_content, html_content):
        email = EmailMultiAlternatives(subject, text_content, from_email, to_email_list)
        if html_content:
            email.attach_alternative(html_content, "text/html")
        email_send_status = email.send()

        email_send_log = EmailSendLog(
            from_email_address=from_email, to_email_address_list=",".join(to_email_list), cc_list=",".join(cc_list),
            bcc_list=",".join(bcc_list), subject=subject, text_content=text_content, html_content=html_content,
            email_send_status=email_send_status
        )
        email_send_log.save()
