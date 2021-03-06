from enum import Enum


class ProductAttributeBehaviorEnum(Enum):
    TEXT = 'Text'  # Text Value
    NUMBER = 'Number'  # Rating / Integer
    DECIMAL = 'Decimal'  # Rating / Integer
    BOOLEAN = 'Boolean'  # Yes / No Attribute
    COLOR = 'Color'  # Specially for color type
    RATING = 'Rating'  # Specially for rating type
    DATE = 'Date'  # For products which have specific date availability
    TIME = 'Time'  # For products which have specific time period in a day availability
    DATE_TIME = 'Date Time'  # For products which have seasonal availability

    @classmethod
    def get_choices(cls):
        return [(enum.value, enum.value) for enum in cls]
