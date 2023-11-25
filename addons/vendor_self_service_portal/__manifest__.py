# -*- coding: utf-8 -*-
{
    'name': "Vendor Self Service Portal",
    'summary': "",
    'description': "",
    'author': "Aakash Vishwakarma",
    'website': "www.linkedin.com/in/aakash-vishwakarma-04b399269",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base','sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/vendor_forecast_view.xml',
        'views/templates.xml',
    ],
}
