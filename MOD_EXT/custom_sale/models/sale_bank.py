# -*- coding: utf-8 -*-

from odoo import fields, models


class SaleOrderPaymentBank(models.Model):
    _name = 'sale.order.bank'
    _description = 'Banco'
    _rec_name = 'name'

    name = fields.Char(string="Nombre")
    active = fields.Boolean(string="Activo")