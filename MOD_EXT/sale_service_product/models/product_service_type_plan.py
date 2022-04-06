# -*- coding: utf-8 -*-

from odoo import fields, models


class ProductServiceTypePlan(models.Model):
    _name = 'product.service.type.plan'
    _description = 'Tipo de Plan'
    _rec_name = 'name'

    name = fields.Char(string='Nombre')
    active = fields.Boolean(string="Activo")
