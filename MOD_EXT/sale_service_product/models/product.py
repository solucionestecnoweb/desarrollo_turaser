# -*- coding: utf-8 -*-
from odoo import fields, models


class ProductCategory(models.Model):
    _inherit = 'product.category'

    type_service = fields.Selection([('ticket', 'Boleto'),
                                     ('hotel', 'Hotel'),
                                     ('car', 'Auto'),
                                     ('excursion', 'Excursion'),
                                     ('tickets', 'Entradas'),
                                     ('Transfer', 'Traslado')
                                     ], string='Tipo de Servicios')
