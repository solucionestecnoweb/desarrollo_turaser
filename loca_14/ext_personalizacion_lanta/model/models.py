# -*- coding: utf-8 -*-

import logging
import json
from odoo.tools import float_is_zero, float_compare, safe_eval, date_utils, email_split, email_escape_char, email_re

from odoo import fields, models, api, exceptions, _
from odoo.exceptions import UserError, ValidationError


_logger = logging.getLogger('__name__')


class AccountMove(models.Model):
    """This model add fields need in the invoice for accounting in Venezuela."""
    _inherit = 'account.move'

    invoice_payments_widget = fields.Text(groups="account.group_account_invoice",
        compute='_compute_payments_widget_reconciled_info')

    @api.depends('type', 'line_ids.amount_residual')
    def _compute_payments_widget_reconciled_info(self):
        for move in self:
            if move.state != 'posted' or not move.is_invoice(include_receipts=True):
                move.invoice_payments_widget = json.dumps(False)
                continue
            reconciled_vals = move._get_reconciled_info_JSON_values()
            if reconciled_vals:
                info = {
                    'title': _('Aplicado'),
                    'outstanding': False,
                    'content': reconciled_vals,
                }
                move.invoice_payments_widget = json.dumps(info, default=date_utils.json_default)
            else:
                move.invoice_payments_widget = json.dumps(False)
            #raise UserError(_(' valor=%s')%move.invoice_payments_widget)