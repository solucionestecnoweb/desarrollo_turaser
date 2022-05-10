# -*- coding: utf-8 -*-

{
    'name': 'Intinerarios de Vuelo',
    'version': '0.1',
    'category': 'Extras Tools',
    'summary': '',
    'description': """ """,
    'author': "INM & LDR Soluciones Tecnológicas y Empresariales C.A",
    'website': "http://www.yourcompany.com",
    'contribuitors': "Bryan Gómez <bryan.gomez1311@gmail.com>",
    'depends': ['sale', 'sale_service_product'],
    'data': [
        'security/ir.model.access.csv',
        'views/itinerary_views.xml',
        'views/sale_views.xml',
        'views/menu_itinerary.xml',
    ],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
