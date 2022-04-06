# -*- coding: utf-8 -*-

from odoo import api, fields, models


class Visa(models.Model):
    _name = 'visa'
    _description = 'visa'
    _rec_name = 'name'

    name = fields.Char(string='Tipo')
    number_visa = fields.Char(string="Nro. de Visa")
    issue_date = fields.Date(string="Fecha de Emision")
    expiration_date = fields.Date(string="Fecha de Vencimiento")
    country_id = fields.Many2one('res.country', string="Pais")
    partner_id = fields.Many2one('res.partner', string="Cliente")
    is_company = fields.Boolean(related="partner_id.is_company")
    image_128 = fields.Image("Image 128", max_width=128, max_height=128, store=True)