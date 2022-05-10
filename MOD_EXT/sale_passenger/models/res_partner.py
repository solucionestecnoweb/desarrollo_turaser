from odoo import fields, models


class Partner(models.Model):
    _inherit = 'res.partner'

    passenger_ids = fields.One2many('passenger', 'partner_id', string='Pasajeros')
