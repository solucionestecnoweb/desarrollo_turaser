from odoo import fields, models


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    passenger_ids = fields.Many2many('passenger', string='Pasajeros')

