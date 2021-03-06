"""
    Created by tareq on ৩/৭/১৯
"""

from allauth.account.models import EmailAddress
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.sites.models import Site
from rest_framework.authtoken.models import Token

__author__ = "Tareq"

admin.site.unregister(EmailAddress)
admin.site.unregister(Group)
admin.site.unregister(Token)
admin.site.unregister(Site)
