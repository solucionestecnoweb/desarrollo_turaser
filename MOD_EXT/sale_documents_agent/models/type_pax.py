# -*- coding: utf-8 -*-
from odoo import api, fields, models


class TypePax(models.Model):
    _name = 'type.pax'
    _description = 'Tipo Pax'
    _rec_name = 'name'

    name = fields.Char(string="Nombre")
    active = fields.Boolean(string="Activo")