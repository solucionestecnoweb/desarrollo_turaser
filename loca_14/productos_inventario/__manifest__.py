# -*- coding: utf-8 -*-
{
    'name': "productos_inventario",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['stock', 'product'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/product_template_views.xml',
        'views/product_eje_views.xml',
        'views/product_motor_litro_views.xml',
        'views/product_montaje_views.xml',
        'views/product_marca_vehiculo_views.xml',
        'views/product_medida_views.xml',
        'views/product_modelo_views.xml',
        'views/product_motor_views.xml',
        'views/product_otras_aplicaciones_views.xml',
        'views/product_motor_views.xml',
        'views/menu_root_views.xml',
    ],

}
