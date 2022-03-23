# -*- coding: utf-8 -*-

from odoo import fields, models


class SaleOrderPaymentCardType(models.Model):
    _name = 'sale.order.card.type'
    _description = 'Tipo Tarjeta'

    name = fields.Char(string="Nombre")
    active = fields.Boolean(string="Activo")