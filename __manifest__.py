# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
#
# Copyright (c) 2018  - Raiden - www.raiden.com.tr

{
    'name': 'Amount to Text Turkish',
    'version': '0.1',
	'price': 5,
	'currency': 'EUR',
    'category': 'Accounting',
    'summary': """This Module converts the amount of the invoice/order to Turkish"""
    'description': """
This Module converts the amount of the invoice/order to Turkish
========================================================================


**Email:** bilgi@raiden.com.tr
""",
    'author': 'Gökhan Aydın',
    'website': 'http://www.raiden.com.tr/',
    'depends': ['account','sale'],
    'data': [
        'views/order_invoice.xml',

    ],

    'installable': True,
    'application': False,
    'auto_install': False,
}
