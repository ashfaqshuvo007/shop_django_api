"""
    Created by tareq on ৩/৭/১৯
"""
from django.contrib import admin
from django.contrib.admin import ModelAdmin

from sol_factory.logs.models import EmailSendLog

__author__ = "Tareq"


@admin.register(EmailSendLog)
class EmailSendLogAdmin(ModelAdmin):
    list_display = [
        'from_email_address', 'to_email_address_list', 'subject', 'email_send_status'
    ]
    fields = [
        'from_email_address', 'to_email_address_list', 'cc_list', 'bcc_list', 'subject', 'text_content', 'html_content',
        'email_send_status'
    ]
