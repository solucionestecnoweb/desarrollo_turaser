# -*- coding: utf-8 -*-

import logging
from odoo import fields, models, api
_logger = logging.getLogger('__name__')


class AccountMove(models.Model):
    _inherit = 'account.move'

    invoice_number_next = fields.Char(string='Nro Invoice')
    invoice_number_control = fields.Char(string='Nro Control')
    invoice_number_unique = fields.Char(string='Nro Control Unique')
    is_delivery_note = fields.Boolean(default=False)
    delivery_note_next_number = fields.Char(string='Nro. Nota de Entrega')
    is_control_unique = fields.Boolean(related='company_id.is_control_unique')
    is_manual = fields.Boolean(string='Numeracion Manual')
    hide_book = fields.Boolean(string='Excluir de Libros')

    _sql_constraints = [
        ('unique_invoice_number_next', 'unique(invoice_number_next)', 'Este numero de Factura ya existe'),
        ('unique_invoice_number_control', 'unique(invoice_number_control)', 'Este numero de control ya existe'),
        ('unique_invoice_number_unique', 'unique(invoice_number_unique)', 'Este numero de control unico ya existe'),
        ('unique_delivery_note_next_number', 'unique(delivery_note_next_number)',
         'Este numero de nota de entregsa ya existe'),
    ]

    @api.onchange('is_delivery_note')
    def _onchange_hide_books(self):
        if self.is_delivery_note:
            self.hide_book = True
        else:
            self.hide_book = False

    def action_post(self):
        res = super(AccountMove, self).action_post()
        if self.is_delivery_note:
            self.delivery_note_next_number = self.get_nro_nota_entrega()
        self.invoice_number_seq()
        self.invoice_control()
        self.invoice_number_control_unique()
        return res

    def invoice_number_seq(self):
        if not self.is_manual:
            if self.move_type in ['out_invoice'] and not self.invoice_number_next:
                self.invoice_number_next = self.get_invoice_number()
            elif self.move_type in ['out_refund'] and not self.invoice_number_next:
                self.invoice_number_next = self.get_refund_number()
            elif self.move_type in ['out_receipt'] and not self.invoice_number_next:
                self.invoice_number_next = self.get_receipt_number()

    def invoice_control(self):
        if not self.is_control_unique or not self.is_manual:
            if self.move_type in ['out_invoice'] and not self.invoice_number_control:
                self.invoice_number_control = self.get_invoice_number_control()
            elif self.move_type in ['out_refund'] and not self.invoice_number_control:
                self.invoice_number_control = self.get_refund_number_control()
            elif self.move_type in ['out_receipt'] and not self.refund_ctrl_number_cli:
                self.invoice_number_control = self.get_receipt_number_control()

    def invoice_number_control_unique(self):
        if self.is_control_unique and not self.is_manual:
            if self.move_type in ['out_invoice'] and not self.invoice_number_unique:
                self.invoice_number_unique = self.get_number_control_unique()
            elif self.move_type in ['out_refund'] and not self.invoice_number_unique:
                self.invoice_number_unique = self.get_number_control_unique()
            elif self.move_type in ['out_receipt'] and not self.invoice_number_unique:
                self.invoice_number_unique = self.get_number_control_unique()

    def get_invoice_number(self):
        self.ensure_one()
        if not self.is_delivery_note:
            seq = self.env['ir.sequence'].get('account.out.invoice')
            return seq
        return ''

    def get_invoice_number_control(self):
        self.ensure_one()
        if not self.is_delivery_note:
            seq = self.env['ir.sequence'].get('account.out.invoice.control')
            return seq
        return ''

    def get_refund_number(self):
        self.ensure_one()
        if not self.is_delivery_note:
            seq = self.env['ir.sequence'].get('account.credit.note')
            return seq
        return ''

    def get_refund_number_control(self):
        self.ensure_one()
        if not self.is_delivery_note:
            seq = self.env['ir.sequence'].get('account.credit.note.control')
            return seq
        return ''

    def get_receipt_number(self):
        self.ensure_one()
        if not self.is_delivery_note:
            seq = self.env['ir.sequence'].get('account.debit.note')
            return seq
        return ''

    def get_receipt_number_control(self):
        self.ensure_one()
        if not self.is_delivery_note:
            seq = self.env['ir.sequence'].get('account.debit.note.control')
            return seq
        return ''

    def get_number_control_unique(self):
        self.ensure_one()
        if not self.is_delivery_note:
            seq = self.env['ir.sequence'].get('account.control.unique')
            return seq
        return ''

    def get_nro_nota_entrega(self):
        self.ensure_one()
        seq = self.env['ir.sequence'].get('account.delivery.note.sequence')
        return seq
