# -*- coding: utf-8 -*-

from odoo import fields, models


class Passport(models.Model):
    _name = 'passport'
    _description = 'Pasaporte'
    _rec_name = 'name'

    name = fields.Char(string="Nro. de Pasaporte")
    issue_date = fields.Date(string="Fecha de Emision")
    expiration_date = fields.Date(string="Fecha de Vencimiento")
    partner_id = fields.Many2one('res.partner', string="Cliente")
    is_company = fields.Boolean(related="partner_id.is_company")
    image_128 = fields.Image("Image 128", max_width=128, max_height=128, store=True)
