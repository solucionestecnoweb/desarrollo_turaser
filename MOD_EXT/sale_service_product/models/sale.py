# -*- coding: utf-8 -*-
from odoo import fields, models, api


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    seller_ids = fields.Many2many('product.supplierinfo', string='Proveedor')
    drive_id = fields.Many2one('res.partner', string='Conductor')
    pax_id = fields .Many2one('type.pax', string='Tipo de Pax')
    product_plan_id = fields.Many2one('product.service.type.plan', string='Plan')
    product_location = fields.Char(string='localizador/PNR-Externo')
    product_rom_id = fields.Many2one('product.service.room', string='Tipo de Habitacion')
    product_gds = fields.Char(string='Gds')
    product_cabin_id = fields.Many2one('product.service.cabin', string='Tipo Cabina')
    product_itinerary = fields.Char(string='Itinerario del Vuelo')
    product_code_id = fields.Many2one('product.service.code', string='Codigo')
    product_event_id = fields.Many2one('product.service.event', string='Evento')
    product_age = fields.Char(string='Edad')
    product_ticket = fields.Char(string='Boleto')
    product_pasarel = fields.Integer(string='Cargo pasarel')
    state_id = fields.Many2one('res.country.state', string='Ubicacion')
    partner_ids = fields.Many2many('res.partner', string='Pasajeros')
    start_date = fields.Date(string='Fecha de Inc')
    end_date = fields.Date(string='Fecha de Out')
    city_id = fields.Many2one('res.city', 'Origen')
    city_id2 = fields.Many2one('res.city', 'destino')
    service_charge = fields.Char(string='cargos por servicio')
    type_service = fields.Selection(related='product_id.categ_id.type_service')

    @api.onchange('product_id')
    def _onchange_seller(self):
        if not self. product_id:
            return
        supplierinfo = self.env['product.supplierinfo'].search([('product_tmpl_id', '=', self.product_id.product_tmpl_id.id)])
        self.seller_ids = supplierinfo.ids


    @api.depends('order_id.state')
    def _compute_invoice_status(self):
        res = super(SaleOrderLine, self)._compute_invoice_status()
        for line in self:
            if line.order_id.state == 'sale' and line.invoice_status == 'no' and \
                    line.product_id.type in ['consu', 'product', 'service']:
                line.invoice_status = 'to invoice'
        return res
