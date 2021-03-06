# -*- coding: utf-8 -*-

{
    'name': 'Custom sale',
    'version': '0.1',
    'category': 'Sale',
    'summary': '',
    'description': """ """,
    'author': "INM & LDR Soluciones Tecnológicas y Empresariales C.A",
    'website': "http://www.yourcompany.com",
    'contribuitors': "Bryan Gómez <bryan.gomez1311@gmail.com>",
    'depends': [
        'sale',
        'product',
        'l10n_ve_base',
        'sale_documents_agent',
        'sale_passenger',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/ir_sequence.xml',
        'views/sale_views.xml',
        'views/sale_bank_views.xml',
        'views/sale_card_type_views.xml',
        'views/sale_payment_views.xml',
        'report/paperformat.xml',
        'report/ir_action_report.xml',
        'wizard/sale_payment_register_views.xml',
        'views/report_sale_voucher.xml',
        'views/report_voucher.xml',
        'views/menu_root.xml',
    ],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
