# -*- coding: utf-8 -*-

from odoo import fields, models


class ProductServiceCode(models.Model):
    _name = 'product.service.code'
    _description = 'Servicio Codigo'
    _rec_name = 'name'

    name = fields.Char(string='Nombre')
    active = fields.Boolean(string="Activo")
