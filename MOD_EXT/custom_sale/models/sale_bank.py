# -*- coding: utf-8 -*-

from odoo import fields, models


class SaleOrderPaymentBank(models.Model):
    _name = 'sale.order.bank'
    _description = 'Banco'

    name = fields.Char(string="Nombre")
    active = fields.Boolean(string="Activo")