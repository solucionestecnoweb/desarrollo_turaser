# -*- encoding: utf-8 -*-
from odoo import fields, models


class ResCity(models.Model):
    _inherit = 'res.city'

    code = fields.Char(string='Codigo', help='The city code')
