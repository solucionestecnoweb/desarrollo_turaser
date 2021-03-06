# -*- coding: utf-8 -*-

{
    'name': 'Servicios de Productos en Ventas',
    'version': '0.1',
    'category': 'Extras Tools',
    'summary': '',
    'description': """ """,
    'author': "INM & LDR Soluciones Tecnológicas y Empresariales C.A",
    'website': "http://www.yourcompany.com",
    'contribuitors': "Bryan Gómez <bryan.gomez1311@gmail.com>",
    'depends': ['sale_documents_agent', 'l10n_ve_base', 'sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/sale_views.xml',
        'views/product_views.xml',
        'views/product_service_cabin_views.xml',
        'views/product_service_code_views.xml',
        'views/product_service_event_views.xml',
        'views/product_service_room_views.xml',
        'views/product_service_type_plan_views.xml',
        'views/menu_root.xml',
    ],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
