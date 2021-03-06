"""
    Created by tareq on 9/28/19
"""

from enum import Enum

__author__ = 'Tareq'


class BaseEnum(Enum):
    """
    BWEnum is the base for all enums in blackwidow project. This class provide some extra functionality added to the
    class Enum.
    """

    @classmethod
    def get_name_from_value(cls, value, default='N/A'):
        """
        Get the name (label) of enum from value
        :param value: value of the enum
        :param default: to return if no value is matched with enum's value
        :return: label of enum if value is found. default otherwise
        """
        from sol_factory.base.utils.tools.titleize import str_titleize

        for e in cls:
            if value == e.value:
                return str_titleize(e.name)
        return default

    @classmethod
    def get_value_from_name_i(cls, name, default=None):
        """
        Get the value of enum from name (label) - case insensitive
        :param name: name (label) of enum
        :param default: to return if no name(label) is matched
        :return: value of enum if name if found. default otherwise
        """
        from sol_factory.base.utils.tools.titleize import str_titleize
        name = name.strip()

        for e in cls:
            if name.lower() == e.name.lower() or name.lower() == str_titleize(e.name).lower():
                return e.value
        return default

    @classmethod
    def get_value_from_name(cls, name, default=None):
        """
        Get the value of enum from name (label)
        :param name: name (label) of enum
        :param default: to return if no name(label) is matched
        :return: value of enum if name if found. default otherwise
        """
        from sol_factory.base.utils.tools.titleize import str_titleize

        for e in cls:
            if name == e.name or name == str_titleize(e.name):
                return e.value
        return default

    @classmethod
    def get_choice_list(cls, include_null=True, empty_label='Select One'):
        """
        This method prepare list of  value, name tuples consisting the items of enums. This can be used for select
        (dropdown) field's options. This method can prepare choice list both with and without initial null value.
        :param include_null: if  true, the first item of the choice list will be an empty value (no pre-selected item)
        :param empty_label: the label to display for initial empty value ('Select One' by default)
        :return: The list of value,name tuple consisting the items of the enum
        """
        from sol_factory.base.utils.tools.titleize import str_titleize

        options = list()
        for e in cls:
            options.append((e.value, str_titleize(e.name)))
        options = sorted(options, key=lambda x: x[1])
        if include_null:
            options = [(None, empty_label)] + options
        return options
