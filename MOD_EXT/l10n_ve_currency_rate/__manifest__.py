# -*- coding: utf-8 -*-
{
    "name": " Venezuela - Currency Rate",
    "version": "14.0.1",
    'author': 'INM & LDR Soluciones Tecnológicas y Empresariales C.A',
    'contribuitors': "Bryan Gómez <bryan.gomez1311@gmail.com>",
    'category': 'Accounting/Accounting',
    "description": """""",
    "maintainer": "Oasis Consultora  C.A",
    "website": "",
    'license': 'LGPL-3',
    "depends": ['product', 'account', 'purchase', 'sale'],
    "data": [
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/res_currency_rate_server_views.xml',
        'views/product_template_views.xml',
        'views/product_pricelist_views.xml',
        'views/product_attribute_views.xml',
        #'views/account_move.xml',
        #'views/sale_order.xml',
        #'views/purchase_order.xml',
        'views/exchange_rate.xml',
    ],
    'qweb': [
        'static/src/xml/*.xml',
    ],
    "installable": True,

}
