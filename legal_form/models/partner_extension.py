from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    legal_form_id = fields.Many2one('legal_form.legal_form', string='Legal Form')

