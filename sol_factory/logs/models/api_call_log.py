"""
    Created by tareq on 9/26/19
"""
import json
from datetime import datetime

from django.db.models import URLField, CharField, TextField, DateTimeField

from sol_factory.base.models import DomainEntity
from sol_factory.logs.models.error_log import ErrorLog

__author__ = "Tareq"


class ApiCallLog(DomainEntity):
    url = URLField()
    request_type = CharField(max_length=500)
    token = CharField(max_length=200)
    request_body = TextField(blank=True)
    request_data = TextField(blank=True)
    response_data = TextField(blank=True)
    response_body = TextField(blank=True)
    extra_info = TextField(blank=True)
    start_time = DateTimeField(blank=True, null=True)
    end_time = DateTimeField(blank=True, null=True)

    class Meta:
        app_label = 'logs'

    @property
    def server_processing_time(self):
        return (self.end_time - self.start_time) if (self.start_time and self.end_time) else 'N/A'

    @classmethod
    def log(cls, *args, url='', type='', token='', log=None, tsync_id=None,
            request=None, response=None, log_time=None, **kwargs):
        try:
            if log is None:
                if tsync_id is not None:
                    log = ApiCallLog.objects.filter(tsync_id=tsync_id).first()
            if log is None:
                log = cls()
            try:
                if log_time is True:  # Start Time
                    log.start_time = datetime.now()
                elif log_time is False:  # End Time
                    log.end_time = datetime.now()
            except:
                pass

            log.url = url if url != '' else request.META['PATH_INFO']
            try:
                log.token = request.user.auth_token.key
            except:
                pass
            log.request_type = type
            if hasattr(request, 'method'):
                log.request_type = request.method
            if (log.request_data is None or log.request_data == '') and \
                    hasattr(request, 'GET') and request.method.lower() == 'get':
                try:
                    if hasattr(request, 'body'):
                        log.request_body = json.dumps(json.loads(request.body.decode("utf-8")))
                except:
                    pass
                log.request_type = type if type != '' else 'GET'
            elif hasattr(request, 'POST') and request.method.lower() == 'post':
                try:
                    if hasattr(request, 'body'):
                        log.request_body = json.dumps(json.loads(request.body.decode("utf-8")))
                except:
                    pass
                log.request_type = type if type != '' else 'POST'
            elif hasattr(request, 'PUT') and request.method.lower() == 'put':
                try:
                    if hasattr(request, 'body'):
                        log.request_body = json.dumps(json.loads(request.body.decode("utf-8")))
                except:
                    pass
                log.request_type = type if type != '' else 'PUT'
            if hasattr(request, 'data') and log.request_type != 'GET':
                log.request_data = request.data
            else:
                try:
                    log.request_data = json.dumps(request.GET)
                except:
                    pass
            if response:
                log.response_data = str(response.status_code) + ' ' + response.status_text
                try:
                    if request.method.lower() != 'get':
                        try:
                            response_body = json.dumps(response.data)
                            if response_body is None:
                                response_body = ''
                        except:
                            response_body = ''
                        log.response_body = response_body
                except Exception as e:
                    ErrorLog.log(exp=e)

            if not log.request_body:
                try:
                    if hasattr(request, 'body'):
                        log.request_body = json.dumps(json.loads(request.body.decode("utf-8")))
                except:
                    pass
            log.save()
            return log

        except Exception as exp:
            ErrorLog.log(exp)
            return None
