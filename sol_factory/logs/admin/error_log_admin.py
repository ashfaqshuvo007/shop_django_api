"""
    Created by tareq on ৩/৭/১৯
"""
from django.contrib import admin
from django.contrib.admin import ModelAdmin

from sol_factory.logs.models import ErrorLog

__author__ = "Tareq"


@admin.register(ErrorLog)
class ErrorLogAdmin(ModelAdmin):
    list_display = [
        'error_message', 'error_code', 'date_created',
    ]
    fields = [
        'message', 'error_code', 'stacktrace'
    ]
