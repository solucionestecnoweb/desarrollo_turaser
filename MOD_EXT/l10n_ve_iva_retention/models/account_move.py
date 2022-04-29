# -*- coding: utf-8 -*-

import logging
from odoo import fields, models
_logger = logging.getLogger('__name__')


class AccountMove(models.Model):
    _inherit = 'account.move'

    retention_iva_id = fields.Many2one('retention.iva', string='Retencion IVA', readonly=True, copy=False)
    state_email_iva = fields.Selection([('send', 'Enviado')])

    def action_post(self):
        res = super(AccountMove, self).action_post()
        self.action_retention()
        return res

    def action_retention(self):
        if not self.retention_iva_id:
            retention_iva_obj = self.env['retention.iva']
            retention_iva_line_obj = self.env['retention.iva.line']
            if self.move_type not in ['entry'] and self.partner_id.people_type \
                    and self.partner_id.property_account_payable_vat_id \
                    and self.partner_id.property_account_receivable_vat_id:
                journal = self.env['account.journal'].search([('type', '=', 'ret_iva')])
                rate = self.partner_id.retention_iva_rate
                self.retention_iva_id = retention_iva_obj.create({
                    'partner_id': self.partner_id.id,
                    'move_id': self.id,
                    'journal_id': journal.id,
                })

                for move in self.invoice_line_ids:
                    base = move.price_subtotal
                    amount_total = move.price_total
                    amount_iva = (amount_total - base)
                    amount_detained = (amount_iva * rate)/100
                    retention_iva_line_obj.create({
                        'retention_iva_id': self.retention_iva_id.id,
                        'amount_tax': base * amount_iva,
                        'amount_retention': base * amount_detained,
                        'retention_rate': rate,
                        'tax_ids': move.tax_ids.ids,
                        'amount_untaxed': self.amount_rate_retention_iva(base)
                    })
                if self.move_type in ['in_invoice', 'in_refund', 'in_receipt']:
                    self.retention_iva_id.action_post()

    def amount_rate_retention_iva(self, amount):
        amount_aux = 0.0
        result = 0.0
        rate = self.env['res.currency.rate'].search(
            [('currency_id', '=', self.currency_id.id), ('name', '<=', self.date)], order="name asc")
        if self.currency_id != self.company_id.currency_id:
            for r in rate:
                if self.date >= r.name:
                    amount_aux += r.rate
            rate = round(1 / amount_aux, 2)
            result += amount * rate
        else:
            result += amount
        return result

    def send_retention_iva(self):
        pass

    def _reverse_moves(self, default_values_list=None, cancel=False):
        res = super(AccountMove, self)._reverse_moves(default_values_list=None, cancel=False)
        res.write({
            'ref': res.id
        })
        return res

    def _check_balanced(self):
        """ Assert the move is fully balanced debit = credit.
            An error is raised if it's not the case.
        """
        moves = self.filtered(lambda move: move.line_ids)
        if not moves:
            return

        # /!\ As this method is called in create / write, we can't make the assumption the computed stored fields
        # are already done. Then, this query MUST NOT depend of computed stored fields (e.g. balance).
        # It happens as the ORM makes the create with the 'no_recompute' statement.
        self.env['account.move.line'].flush(self.env['account.move.line']._fields)
        self.env['account.move'].flush(['journal_id'])
        self._cr.execute('''
            SELECT line.move_id, ROUND(SUM(line.debit - line.credit), currency.decimal_places)
            FROM account_move_line line
            JOIN account_move move ON move.id = line.move_id
            JOIN account_journal journal ON journal.id = move.journal_id
            JOIN res_company company ON company.id = journal.company_id
            JOIN res_currency currency ON currency.id = company.currency_id
            WHERE line.move_id IN %s
            GROUP BY line.move_id, currency.decimal_places
            HAVING ROUND(SUM(line.debit - line.credit), currency.decimal_places) != 0.0;
        ''', [tuple(self.ids)])

        query_res = self._cr.fetchall()
        if query_res:
            ids = [res[0] for res in query_res]
            sums = [res[1] for res in query_res]
