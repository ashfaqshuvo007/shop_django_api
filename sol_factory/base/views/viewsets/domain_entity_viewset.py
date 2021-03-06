"""
    Created by tareq on 9/26/19
"""
from django.views.decorators.csrf import csrf_exempt
from rest_framework.viewsets import ModelViewSet

from sol_factory.logs.models import ApiCallLog

__author__ = "Tareq"


class DomainEntityViewSet(ModelViewSet):

    def __init__(self, **kwargs):
        super(DomainEntityViewSet, self).__init__(**kwargs)
        self.sort_by = '-last_updated'

    def get_queryset(self):
        queryset = super(DomainEntityViewSet, self).get_queryset()
        return queryset.order_by(self.sort_by)

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        log = ApiCallLog.log(request=request, log_time=True)
        if log:
            self._log = log
        return super(DomainEntityViewSet, self).dispatch(request, *args, **kwargs)

    def finalize_response(self, request, response, *args, **kwargs):
        log = getattr(self, "_log", None)
        log = ApiCallLog.log(request=request, response=response, log=log, log_time=False)
        if log:
            self._log = log
        return super(DomainEntityViewSet, self).finalize_response(request, response, *args, **kwargs)
