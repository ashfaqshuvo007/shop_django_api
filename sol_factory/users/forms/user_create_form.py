"""
    Created by tareq on ১৪/৬/১৯
"""
from django.contrib.auth.forms import UserCreationForm

from sol_factory.users.models import ConsoleUser

__author__ = "Tareq"


class ConsoleUserCreateForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = ConsoleUser
        fields = ('username', 'email', 'first_name', 'last_name')
