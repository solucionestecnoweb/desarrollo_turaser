# -*- coding: utf-8 -*-
{
    'name': "purchase_stock",

    'summary': """
    Se agregan campos de numero de parte y codigo de barra """,

    'description': """
        Numero de parte y codigo de barra campos adicionales al
        seleccionar el producto 
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'stock', 'product'],

    # always loaded
    'data': [
        'views/views.xml',
    ],

}
