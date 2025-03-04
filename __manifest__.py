# -*- coding: utf-8 -*-
{
    'name': "Client Spec",

    'summary': """Gestion Clients Grossistes""",

    'description': """
        Gestion client grossiste module pour :
            - Gerer client et commandes
            - Gerer assurances            
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded    .xml & .csv
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'templates.xml',
        'views/clientspec.xml',
	    'reports.xml',
    ],

    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}
