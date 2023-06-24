# -*- coding: utf-8 -*-
{
    'name': "Capital",
    'summary': """
        Capital form in company's and partenrs information.""",
    'description': """
        Add a new field in the company's and partner information.""",
    'author': "Franck Patissier",
    'website': "",
    'category': 'Technical',
    'version': '0.1',
    'license': 'GPL-3',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/company_extension_view.xml',
        'views/partner_extension_view.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'images': ['static/description/icon.png'],
    'installable': True,
    'application': False,
    'auto_install': False,
}
