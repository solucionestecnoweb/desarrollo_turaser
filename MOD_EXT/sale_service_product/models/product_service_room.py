# -*- coding: utf-8 -*-

from odoo import fields, models


class ProductServiceRoom(models.Model):
    _name = 'product.service.room'
    _description = 'Tipo de Habitacion'
    _rec_name = 'name'

    name = fields.Char(string='Nombre')
    active = fields.Boolean(string="Activo")