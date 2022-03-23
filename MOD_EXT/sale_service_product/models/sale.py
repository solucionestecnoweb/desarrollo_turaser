# -*- coding: utf-8 -*-
from odoo import fields, models


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    partner_id = fields.Many2one('res.partner', string='Proveedor', domain=[('travel_agency', '=', True)])
    drive_id = fields.Many2one('res.partner', string='Conductor')
    pax_id = fields .Many2one('type.pax', string='Tipo de Pax')
    product_plan_id = fields.Many2one('product.service.type.plan', string='Plan')
    product_location_id = fields.Many2one('product.service.location', string='localizador')
    product_rom_id = fields.Many2one('product.service.room', string='Tipo de Habitacion')
    product_gds_id = fields.Many2one('product.service.gds', string='Gds')
    product_cabin_id = fields.Many2one('product.service.cabin', string='Tipo Cabina')
    product_itinerary_id = fields.Many2one('product.service.flight.itinerary', string='Itinerario del Vuelo')
    product_code_id = fields.Many2one('product.service.code', string='Codigo')
    product_event_id = fields.Many2one('product.service.event', string='Evento')
    product_age = fields.Char(string='Edad')
    product_pasarel_id = fields.Many2one('product.service.ticket')
    product_ticket_id = fields.Many2one('product.service.pasarel')
    state_id = fields.Many2one('res.country.state', string='Ubicacion')
    partner_ids = fields.Many2many('res.partner', string='Pasajeros')
    start_date = fields.Date(string='Fecha de Inc')
    end_date = fields.Date(string='Fecha de Out')
    street = fields.Char(string="Origen")
    street2 = fields.Char(string="Destino")
    service_charge = fields.Char(string='cargos por servicio')
    type_service = fields.Selection(related='product_id.categ_id.type_service')
