{
    'name': "Sale Order Multi Product Selection",
    'version': "14.0.0.1",
    'summary': "This module allows you to select Multiple product in sale order at a time on single click.",
    'category': 'Sale Management',
    'description': """
        This module allows you to select Multiple product in sale order on single click.
         sale order add multi product
         product add
         multiple product add in sale order quickly
         easy add product in sale order on single click
         create sale order from product
    """,
    'author': "Bryan Gómez",
    'contribuitors': "Bryan Gómez <bryan.gomez1311@gmail.com>",
    'website': "",
    'depends': ['sale_management', 'product'],
    'data': [
        'security/ir.model.access.csv',
        'wizard/multi_product.xml',
        'views/sale.xml',

    ],
    'price': 30.0,
    'currency': 'USD',
    'license': 'OPL-1',
    'installable': True,
    'application': False,
    'auto_install': False,
}
# -*- coding: utf-8 -*-
