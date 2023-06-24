from odoo import models, fields

class ResCompany(models.Model):
    _inherit = 'res.company'

    capital_type = fields.Selection([
        ('fixed_capital', 'Fixed capital'),
        ('open_end_investment', 'Open-end investment'),
        ], string='Capital type')
    capital = fields.Float(string="Capital")
