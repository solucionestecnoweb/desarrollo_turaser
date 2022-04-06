# -*- coding: utf-8 -*-
from odoo import api, fields, models


class TypeBaggage(models.Model):
    _name = 'type.baggage'
    _rec_name = 'name'
    _description = 'Tipo Pax'

    name = fields.Char(string="Nombre")
    description = fields.Char(string="descripcion")
    active = fields.Boolean(string="Activo")