"""
    Created by tareq on ৩/৭/১৯
"""
from django.contrib import admin
from django.contrib.admin import ModelAdmin

from sol_factory.logs.models import ApiCallLog

__author__ = "Tareq"


@admin.register(ApiCallLog)
class ApiCallLogAdmin(ModelAdmin):
    list_display = [
        'url', 'request_type', 'response_data', 'start_time', 'end_time', 'server_processing_time'
    ]
    fields = [
        'url', 'request_type', 'token', 'request_body', 'request_data', 'response_body', 'response_data', 'start_time',
        'end_time'
    ]
