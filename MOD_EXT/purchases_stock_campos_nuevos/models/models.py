# -*- coding: utf-8 -*-

from odoo import models, fields
from odoo import api


class Purchase_Order(models.Model):
    _inherit = "purchase.order.line"

    product_numero_parte = fields.Char(string='Numero de Parte', compute='_compute_nro_parte')
    product_codigo_barras = fields.Char( string='Código de Barras', readonly=1)

    @api.onchange('product_id')
    def _compute_nro_parte(self):
        for rec in self:
            rec.product_numero_parte=rec.product_id.product_numero_parte
            rec.product_codigo_barras=rec.product_id.barcode

