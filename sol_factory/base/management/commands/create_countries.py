"""
    Created by tareq on ২/৭/১৯
"""
from django.core.management import BaseCommand

from sol_factory.base.models import Country
from sol_factory.base.utils.extras.country_list import COUNTRY_NAMES

__author__ = "Tareq"


class Command(BaseCommand):
    def handle(self, *args, **options):
        for c in COUNTRY_NAMES:
            country = Country.objects.filter(name=c).first()
            if country:
                print("{} already exists".format(c, ))
            else:
                country = Country(name=c)
                country.save()
                print("{} created".format(c, ))
