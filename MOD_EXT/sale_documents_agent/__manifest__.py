# -*- coding: utf-8 -*-

{
    'name': 'Documentos Agentes',
    'version': '0.1',
    'category': 'Extras Tools',
    'summary': '',
    'description': """ """,
    'author': "INM & LDR Soluciones Tecnológicas y Empresariales C.A",
    'website': "http://www.yourcompany.com",
    'contribuitors': "Bryan Gómez <bryan.gomez1311@gmail.com>",
    'depends': ['base', 'sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/type_pax_views.xml',
        'views/type_baggage_views.xml',
        'views/promotion_views.xml',
        'views/res_partner_views.xml',
        'views/profession_views.xml',
        'views/menu_root.xml',
    ],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
