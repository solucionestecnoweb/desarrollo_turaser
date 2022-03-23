# -*- coding: utf-8 -*-

from odoo import fields, models


class ProductServiceFlightItinerary(models.Model):
    _name = 'product.service.flight.itinerary'
    _description = 'Itinerario Vuelo'
    _rec_name = 'name'

    name = fields.Char(string='Nombre')
    active = fields.Boolean(string="Activo")
