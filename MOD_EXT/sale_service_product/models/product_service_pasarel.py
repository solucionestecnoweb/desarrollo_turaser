# -*- coding: utf-8 -*-

from odoo import fields, models


class ProductServicePasarel(models.Model):
    _name = 'product.service.pasarel'
    _description = 'Servicio Pasarel'
    _rec_name = 'name'

    name = fields.Char(string='Nombre')
    active = fields.Boolean(string="Activo")