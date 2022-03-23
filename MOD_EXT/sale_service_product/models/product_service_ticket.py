# -*- coding: utf-8 -*-

from odoo import fields, models


class ProductServiceTicket(models.Model):
    _name = 'product.service.ticket'
    _description = 'Servicio Boleto'
    _rec_name = 'name'

    name = fields.Char(string='Numero')
    active = fields.Boolean(string="Activo")
