# -*- coding: utf-8 -*-

from odoo import fields, models


class Partner(models.Model):
    _inherit = 'res.partner'

    visa_ids = fields.One2many('visa', 'partner_id', string='Visas')
    passport_ids = fields.One2many('passport', 'partner_id', string='Pasaportes')
