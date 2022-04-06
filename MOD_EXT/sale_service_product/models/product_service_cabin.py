# -*- coding: utf-8 -*-

from odoo import fields, models


class ProductServiceCabin(models.Model):
    _name = 'product.service.cabin'
    _description = 'Tipo Cabina'
    _rec_name = 'name'

    name = fields.Char(string='Nombre')
    active = fields.Boolean(string="Activo")
