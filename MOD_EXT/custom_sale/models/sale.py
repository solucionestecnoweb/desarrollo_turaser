# -*- coding: utf-8 -*-

from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    # Partner
    vat = fields.Char(related='partner_id.vat')
    vat2 = fields.Char(related='partner_id.vat2')
    email = fields.Char(related='partner_id.email')
    company_type = fields.Selection(related='partner_id.company_type', store=True)

    # User Partner
    mobile = fields.Char(related='user_id.partner_id.phone')
    phone = fields.Char(related='user_id.partner_id.phone')
    user_email = fields.Char(related='user_id.partner_id.email')

    pnr = fields.Char(string="PNR")
    is_service = fields.Boolean(string="Extension de Servicio")
    parent_id = fields.Many2one('sale.order', string="Documento origen")
    seller_id = fields.Many2one('res.partner', string="Enterado por")
    sale_payment_id = fields.Many2one('sale.order.payment', string="Pago")
    promotion_id = fields.Many2one('promotion', string="Promocion")
    number_promotion = fields.Char(string="Nro. de Promocion")
    state = fields.Selection(selection_add=[
        ('payment_pending', 'Servicio Pendiente de Pago'),
        ('service_for_approved', 'Servicio por Aprobar'),
        ('service_approved', 'Servicio Aprobado'),
        ('service_issue_voucher', 'Servicio por Emitir Voucher'),
        ('voucher_issue', 'Voucher Emitido'),
        ('pre_invoice', 'Pre-Factura'),
        ('invoice', 'Factura'),
    ],
        ondelete={
            'payment_pending': 'set default',
            'service_for_approved': 'set default',
            'service_approved': 'set default',
            'service_issue_voucher': 'set default',
            'voucher_issue': 'set default',
            'pre_invoice': 'set default',
            'invoice': 'set default',
    })

    def action_payment_for_approval(self):
        self.write({'state': 'service_in_approved'})

    def action_payment_approval(self):
        self.write({'state': 'service_approved'})

    def action_voucher_issue(self):
        self.write({'state': 'service_issue_voucher'})

    def action_validate_voucher(self):
        self.write({'state': 'voucher_issue'})

    def action_validate_pre_invoice(self):
        self.write({'state': 'pre_invoice'})

    def action_sale_register_payment(self):
        return {
            'name': 'Registro de Pagos',
            'res_model': 'sale.order.payment.register',
            'view_mode': 'form',
            'context': {
                'default_partner_id': self.partner_id.id,
                'default_sale_id': self.id,
                'default_amount': self.amount_total,
            },
            'target': 'new',
            'type': 'ir.actions.act_window',
        }
