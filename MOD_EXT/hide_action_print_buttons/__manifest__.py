# -*- coding: utf-8 -*-

{
    'name': "Hide Action/Print Buttons",
    'summary': """
        This module give user restriction to Show/Hide Action/Print buttons per user""",
    'description': """
        This module help to give permission to user to show Action/Print buttons in all modules
    """,

    'author': "INM & LDR Soluciones Tecnológicas y Empresariales C.A",
    'website': "http://www.yourcompany.com",
    'contribuitors': "Bryan Gómez <bryan.gomez1311@gmail.com>,  Ing Johan Morey",
    'category': "Extra Tools",
    'version': '14.0',
    'depends': ['base','web'],
    'qweb': ["static/src/xml/base.xml"],
    'data': [
        'views/templates.xml',
        'security/security.xml',
    ],
    "images": ['static/description/icon.png'],

}
