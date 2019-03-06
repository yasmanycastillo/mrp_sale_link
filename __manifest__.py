# -*- coding: utf-8 -*-
{
    'name': "MRP sale link",

    'summary': """
        This module add sale order link in production view..""",

    'description': """
    """,

    'author': "Yasmany Castillo",
    'website': "",

    'category': 'Manufacturing',
    'version': '11.0.1.0',
    # any module necessary for this one to work correctly
    'depends': ['mrp', 'sale_mrp'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/mrp_production_views.xml',
    ],
}
