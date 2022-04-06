# -*- coding: utf-8 -*-

from odoo import api, fields, models


class Promotion(models.Model):
    _name = 'promotion'
    _description = 'Promociones'
    _rec_name = 'name'

    name = fields.Char(string='Nombre')
    active = fields.Boolean(string="Activo")
