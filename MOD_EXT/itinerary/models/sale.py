from odoo import fields, models


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    itinerary_ids = fields.One2many('itinerary', 'sale_line_id', string='Itinerarios')
