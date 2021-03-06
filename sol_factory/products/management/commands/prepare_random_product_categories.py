"""
    Created by tareq on ২৮/৬/১৯
"""
from django.core.management import BaseCommand

from sol_factory.products.models import ProductCategory

__author__ = "Tareq"

CATEGORIES_LIST = [
    {
        'name': 'Service',
        'child': [
            {
                'name': 'Environmental Department Consultancy',
                'child': []
            },
            {
                'name': 'Gas Connection Consultancy',
                'child': []
            },
            {
                'name': 'Project Consultancy',
                'child': []
            },
            {
                'name': 'Government Regulatory Consultancy',
                'child': []
            },
        ]
    },
    {
        'name': 'Construction Material',
        'child': [
            {
                'name': 'Building & Construction Machines',
                'child': []
            },
            {
                'name': 'Metal Pipe & Plumbing Fittings‎',
                'child': []
            },
            {
                'name': 'Doors and Windows‎',
                'child': []
            },
            {
                'name': 'Brackets, Holder & Hardware Fittings‎',
                'child': []
            },
            {
                'name': 'Cranes, Forklift & Lifting Machines',
                'child': []
            },
            {
                'name': 'Paints, Wall Putty & Varnishes‎',
                'child': []
            },
        ]
    },
    {
        'name': 'Optical Fiber, Cable & Wire',
        'child': [
            {
                'name': 'Electric Wire & Cable',
                'child': []
            },
            {
                'name': 'Optical Fiber',
                'child': []
            },
            {
                'name': 'Communication Cable',
                'child': []
            },
            {
                'name': 'Power Cable',
                'child': []
            },
            {
                'name': 'Audio & Video Cable',
                'child': []
            },
            {
                'name': '33kV Cable',
                'child': []
            },
            {
                'name': '11kV Cable',
                'child': []
            },
            {
                'name': '132kV Cable',
                'child': []
            },
        ]
    },
    {
        'name': 'Motors',
        'child': [
            {
                'name': 'Electric Motor',
                'child': []
            },
            {
                'name': 'AC Motor',
                'child': []
            },
            {
                'name': 'DC Motor',
                'child': []
            },
            {
                'name': 'Asynchronous Motor',
                'child': []
            },
            {
                'name': 'Stepper Motor',
                'child': []
            },
            {
                'name': 'Servo Motor',
                'child': []
            },
        ]
    },
    {
        'name': 'Power Supply & Distribution',
        'child': [
            {
                'name': 'Power Transmission & Transformer',
                'child': []
            },
            {
                'name': 'Power Adaptor',
                'child': []
            },
            {
                'name': 'Relay & Contactor',
                'child': []
            },
            {
                'name': 'LED Power Supply',
                'child': []
            },
            {
                'name': 'Voltage Regulator',
                'child': []
            },
        ]
    },
    {
        'name': 'Telecom & Broadcasting',
        'child': [
            {
                'name': 'Fiber Optic Equipment',
                'child': []
            },
            {
                'name': 'Communication Module',
                'child': []
            },
            {
                'name': 'Antenna',
                'child': []
            },
            {
                'name': 'Radio & TV Broadcasting',
                'child': []
            },
            {
                'name': 'Satellite',
                'child': []
            },
        ]
    },
    {
        'name': 'Electronic Components',
        'child': [
            {
                'name': 'Connector & Terminals',
                'child': []
            },
            {
                'name': 'Switch',
                'child': []
            },
            {
                'name': 'Circuit Board',
                'child': []
            },
            {
                'name': 'Sensor',
                'child': []
            },
            {
                'name': 'Breaker & Protector',
                'child': []
            },
            {
                'name': 'Socket & Outlet',
                'child': []
            },
            {
                'name': 'Transformer',
                'child': []
            },
            {
                'name': 'Inverter',
                'child': []
            },
            {
                'name': 'Terminals',
                'child': []
            },
            {
                'name': 'Remote Control',
                'child': []
            },
            {
                'name': 'Capacitor',
                'child': []
            },
            {
                'name': 'Electronic Tube & Transistor',
                'child': []
            },
            {
                'name': 'Level Transmitter',
                'child': []
            },
            {
                'name': 'Level Switch',
                'child': []
            },
            {
                'name': 'Pressure Transmitter',
                'child': []
            },
            {
                'name': 'Pressure Switch',
                'child': []
            },
        ]
    },
]


class Command(BaseCommand):
    def create_categories(self, parent=None, categories=[]):
        for _category in categories:
            _name = _category.get('name')
            print(_name)
            category = ProductCategory.objects.filter(name=_name).last()
            if category:
                print("Already exists. Skipping...")
            else:
                category = ProductCategory(name=_name)
                category.parent = parent
                category.save()
                print("Created.")
            self.create_categories(parent=category, categories=_category.get('child'))

    def handle(self, *args, **options):
        self.create_categories(parent=None, categories=CATEGORIES_LIST)
