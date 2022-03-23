# -*- coding: utf-8 -*-
from odoo import api, fields, models


class TypePax(models.Model):
    _name = 'type.pax'
    _rec_name = 'name'
    _description = 'Tipo Pax'

    name = fields.Char(string="Nombre")
    active = fields.Boolean(string="Activo")