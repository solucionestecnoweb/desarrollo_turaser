# -*- coding: utf-8 -*-

from odoo import fields, models


class ProductServiceGds(models.Model):
    _name = 'product.service.gds'
    _description = 'GDS'
    _rec_name = 'name'

    name = fields.Char(string='Nombre')
    active = fields.Boolean(string="Activo")