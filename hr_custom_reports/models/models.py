# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class hr_custom_reports(models.Model):
#     _name = 'hr_custom_reports.hr_custom_reports'
#     _description = 'hr_custom_reports.hr_custom_reports'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
