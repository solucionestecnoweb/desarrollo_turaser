# -*- coding: utf-8 -*-

from odoo import fields, models


class ProductServiceEvent(models.Model):
    _name = 'product.service.event'
    _description = 'Servicio Evento'
    _rec_name = 'name'

    name = fields.Char(string='Nombre')
    active = fields.Boolean(string="Activo")
