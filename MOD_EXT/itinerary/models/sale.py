from odoo import fields, models


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    origin_id = fields.Many2one('itinerary.origin', string='origen')
    destination = fields.Many2one('itinerary.destination', string='destino')
    duration_flight = fields.Float(string='Duracion de Viaje')
    arrival_time = fields.Datetime('Hora de llegada', default=lambda self: fields.Datetime.now())
    exit_time = fields.Datetime('Hora de Salida')

