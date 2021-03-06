"""
    Created by tareq on 9/26/19
"""
import traceback

from django.db.models import TextField
from django.utils.safestring import mark_safe

from sol_factory.base.models import DomainEntity

__author__ = "Tareq"


class ErrorLog(DomainEntity):
    message = TextField(blank=True)
    error_code = TextField(blank=True)
    stacktrace = TextField(null=True)

    class Meta:
        app_label = 'logs'

    @property
    def error_message(self):
        return mark_safe(self.message)

    @classmethod
    def log(cls, exp, *args, **kwargs):
        log = cls()
        log.message = str(exp)
        log.error_code = ""
        log.stacktrace = "\n\n".join(traceback.format_exc().splitlines()) if kwargs.get(
            "stacktrace") is None else kwargs.get("stacktrace")
        log.save()
        return log
