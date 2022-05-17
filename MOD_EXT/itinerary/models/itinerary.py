from odoo import fields, models, api
from datetime import datetime
import pytz


class Itinerary(models.Model):
    _name = 'itinerary'
    _description = 'itinerario'
    _rec_name = 'id'

    sequence = fields.Integer(default=10)
    origin_id = fields.Many2one('itinerary.origin', string='origen')
    sale_line_id = fields.Many2one('sale.order.line', string='linea de pedido')
    destination_id = fields.Many2one('itinerary.destination', string='destino')
    duration_flight = fields.Float(string='Duracion de Viaje', compute='_compute_difference_hours', store=True)
    arrival_time = fields.Datetime('Hora de llegada')
    exit_time = fields.Datetime('Hora de Salida', default=lambda self: fields.Datetime.now())

    @api.depends('arrival_time', 'exit_time')
    def _compute_difference_hours(self):
        for t in self:
            if t.arrival_time and t.exit_time:
                tz_caracas = pytz.timezone('America/Caracas')
                date_out = t.arrival_time.astimezone(tz_caracas).replace(tzinfo=None)
                date_in = t.exit_time.astimezone(tz_caracas).replace(tzinfo=None)
                b = datetime.strptime(str(date_out), '%Y-%m-%d %H:%M:%S')
                a = datetime.strptime(str(date_in), '%Y-%m-%d %H:%M:%S')
                t3 = a - b
                x = int(t3.days) * 24 + (int(t3.seconds) / 3600)
                t.duration_flight = float(abs(x))


class ItineraryOrigin(models.Model):
    _name = 'itinerary.origin'
    _description = 'Origen'
    _rec_name = 'name'

    name = fields.Char(string='Nombre')
    code = fields.Char(string='Codigo')


class ItineraryDestination(models.Model):
    _name = 'itinerary.destination'
    _description = 'destino'
    _rec_name = 'name'

    name = fields.Char(string='Nombre')
    code = fields.Char(string='Codigo')

