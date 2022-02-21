# -*- coding: utf-8 -*-
from odoo import models, fields, api


class AccountMove(models.Model):
    _inherit = 'account.move'

    is_delivery_note = fields.Boolean(default=False)
    delivery_note_next_number = fields.Char(string='Nro. Nota de Entrega')
    doc_currency_id = fields.Many2one("res.currency", string="Moneda del documento Fisico")

    def action_post(self):
        res = super(AccountMove, self).action_post()
        if self.is_delivery_note:
            self.delivery_note_next_number = self.get_nro_nota_entrega()
        return res

    def get_nro_nota_entrega(self):
        self.ensure_one()
        seq = self.env['ir.sequence'].get('account.delivery.note.sequence')
        return seq

    @api.onchange('is_delivery_note')
    def _onchange_hide_books(self):
        if self.is_delivery_note:
            self.ocultar_libros = True
        else:
            self.ocultar_libros = False

