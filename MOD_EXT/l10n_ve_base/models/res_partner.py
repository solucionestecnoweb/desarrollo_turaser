# -*- coding: utf-8 -*-

from odoo import fields, models


class Partner(models.Model):
    _inherit = 'res.partner'

    vat2 = fields.Char(string="Cedula")
    birth_date = fields.Date(string="Fecha de Nacimiento")
    gender = fields.Selection(string="Genero", selection=[('F', 'Femenino'), ('M', 'Masculino'), ('other', 'Otros')])
    nationality_id = fields.Many2one('res.country', string="Nacionalidad")
    lang_id = fields.Many2one('res.lang', string='Idioma')
    travel_agency = fields.Boolean(string='Agencia de Viaje')
    seller = fields.Boolean(string='Vendedor')
