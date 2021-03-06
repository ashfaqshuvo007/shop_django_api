# Created by shamilsakib at 10/19/19
from django.contrib import admin
from django.contrib.admin import ModelAdmin

from sol_factory.sponsors.models import FeaturedCategory


@admin.register(FeaturedCategory)
class FeaturedCategoryAdmin(ModelAdmin):
    list_display = ('category', 'is_master', 'is_published')
    fields = ('category', 'icons', 'is_master', 'is_published')
