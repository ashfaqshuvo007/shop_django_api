"""
    Created by tareq on ২০/৯/১৯
"""
from django.contrib import admin
from django.contrib.admin import ModelAdmin

from sol_factory.users.models import Company, UserProfileInfo

__author__ = "Tareq"

#
# class ProfileInfoInline(admin.TabularInline):
#     model = UserProfileInfo
#

@admin.register(Company)
class CompanyAdmin(ModelAdmin):
    list_display = [
        'name', 'city_name', 'operational_country'
    ]
    fields = [
        'name', 'registered_country', 'operational_country', 'city_name', 'zip_code', 'address', 'number_of_employees',
        'registration_year', 'company_website', 'annual_revenue', 'photo'
    ]
    # inlines = [ProfileInfoInline]
