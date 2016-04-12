# -*- coding: utf-8 -*-
##############################################################################
#
#    Vincent Maraba
#
##############################################################################


{
    'name': 'Aviimo Updates',
    'version': '1.0',
    'category': 'Purchase Order',
    'sequence': 7,
    'summary': 'Implementation of SKU + Lot Number of Barcode use',
    'description': """

=======================

This module adds an activity to the expenses

""",
    'author': 'Innova Africa Ltd',
    'website': 'http://www.innova-africa.net',
    'depends': ['product','purchase','base'],
    'data': [
        'purchase_view.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'auto_install': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
