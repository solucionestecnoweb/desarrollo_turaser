{
    'name': "hide buttons",
    'summary': """ """,
    'description': """ """,
    'author': "INM & LDR Soluciones Tecnológicas y Empresariales C.A",
    'website': "http://www.yourcompany.com",
    'contribuitors': "Bryan Gómez <bryan.gomez1311@gmail.com>",
    'category': "Extra Tools",
    'version': '0.1',
    'depends': ['account', 'sale', 'sale_stock', 'purchase', 'account_debit_note', 'product'],
    'data': [
        'security/account_security.xml',
        'views/sale_views.xml',
        'views/account_payment_views.xml',
        'views/res_partner_views.xml',
        'views/account_views.xml',
        'views/product_template_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
# -*- coding: utf-8 -*-
