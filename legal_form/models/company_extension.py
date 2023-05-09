from odoo import models, fields

class ResCompany(models.Model):
    _inherit = 'res.company'

    capital_type = fields.Selection([
        ('fixed_capital', 'Fixed capital'),
        ('open_end_investment', 'Open-end investment'),
        ], string='Type')
    capital = fields.Float(string="Capital")

    legal_form_id = fields.Many2one('legal_form.legal_form', string='Legal Form')

