# -*- coding: utf-8 -*-
{
    'name': "Venezuela - Account Reports",
    'description': """Account reports for Venezuela""",
    'version': '1.1',
    'author': 'INM & LDR Soluciones Tecnológicas y Empresariales C.A',
    'contribuitors': "Bryan Gómez <bryan.gomez1311@gmail.com>",
    'category': 'Accounting/Localizations/Reporting',
    'website': 'http://soluciones-tecno.com/',
    'depends': ['account', 'l10n_ve_account_sequence_number'],
    'data': [
        'report/paperformat.xml',
        'report/ir_action_report.xml',
        'views/report_account_invoice.xml',
        #'views/report_account_invoice_delivery_note.xml',
    ],
    'application': False,
    'auto_install': False,
}
