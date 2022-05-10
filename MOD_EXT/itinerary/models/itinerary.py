from odoo import fields, models


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

