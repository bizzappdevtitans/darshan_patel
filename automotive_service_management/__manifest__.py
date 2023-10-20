# -*- coding: utf-8 -*-
{
    'name': "automotive_service_management",

    'summary': """Automotive Service Management""",

    'description': """
        Automotive Service Management
    """,

    'author': "BizzAppDev System Pvt. Ltd.",
    'website': "http://www.BizzAppDev.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'version': '15.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/service_appointment_data.xml',
        'views/service_appointment_views.xml',
        'wizard/book_service_appointment_views.xml',
        'wizard/cancel_service_appointment_views.xml',
        'views/automotive_accessories_views.xml',
        'views/automotive_mechanics_views.xml',
        'views/automotive_service_main_menu_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/accessories_data.xml',
    ],
    "license": "LGPL-3",
}
