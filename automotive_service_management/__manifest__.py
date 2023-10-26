# -*- coding: utf-8 -*-
{
    'name': "automotive_service_management",

    'summary': """Automotive Service Management""",

    'description': """
        Automotive Service Management
    """,

    'author': "BizzAppDev System Pvt. Ltd.",
    'website': "http://www.BizzAppDev.com",

    'version': '15.0.0.1',

    'depends': ['base', 'mail'],

    'data': [
        'security/ir.model.access.csv',
        'data/service_appointment_data.xml',
        'data/ir_config_parameter.xml',
        'wizard/service_payment_views.xml',
        'views/service_appointment_views.xml',
        'wizard/book_service_appointment_views.xml',
        'wizard/cancel_service_appointment_views.xml',
        'views/automotive_accessories_views.xml',
        'views/automotive_mechanics_views.xml',
        'data/mail_template_data.xml',
        'views/automotive_service_main_menu_view.xml',
    ],
    'demo': [
        'demo/accessories_data.xml',
    ],
    "license": "LGPL-3",
}
