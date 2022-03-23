# -*- coding: utf-8 -*-

from odoo import fields, models


class ProductServiceLocation(models.Model):
    _name = 'product.service.location'
    _description = 'Localizador'
    _rec_name = 'name'

    name = fields.Char(string='Nombre')
    active = fields.Boolean(string="Activo")