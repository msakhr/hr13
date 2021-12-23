# -*- coding: utf-8 -*-
{
    'name': "HR Custom Reports",

    'summary': """
        HR Customized Reports for Sutherland""",

    'description': """
        HR Customized Reports for Sutherland
    """,

    'author': "Egymentors",
    'website': "http://www.egymentors.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','egymentors_hr','hr_rules','tags__rule','report_xlsx','hr','hr_payroll'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'reports/report_payslip_employee_pdf.xml',
        'reports/reports.xml',
    ],
}
