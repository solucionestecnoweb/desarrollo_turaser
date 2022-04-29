# -*- coding: utf-8 -*-

from odoo import fields, models


class SaleOrderPaymentRegister(models.Model):
    _name = 'sale.order.payment.register'
    _description = 'Registro Pago Ventas'

    partner_id = fields.Many2one('res.partner', string='Cliente')
    sale_id = fields.Many2one('sale.order', string='Pedido de Venta')
    card_type_id = fields.Many2one('sale.order.card.type', string='Tipo de Tarjeta')
    bank_id = fields.Many2one('sale.order.bank', string='Banco')
    payment_method_id = fields.Many2one('sale.order.payment.method', string='Metodo de Pago')
    vat2 = fields.Char(related='partner_id.vat2', string='Numero de Cedula')
    date = fields.Date(string='Fecha')
    cardholder = fields.Char(string='Tarjetahabiente')
    code_security = fields.Char(string='Codigo de Seguridad')
    account_holder = fields.Char(string='Titular de Cuenta')
    number_approval = fields.Char(string='Numero de aprobacion')
    amount = fields.Float(string='Monto')
    image = fields.Binary(string='imagen', store=True, attachment=True)
    serial = fields.Text(string='Seriales')

    def create_payment(self):
        payment_val = {
            'partner_id': self.partner_id.id,
            'card_type_id': self.card_type_id.id,
            'bank_id': self.bank_id.id,
            'sale_id': self.sale_id.id,
            'payment_method_id': self.payment_method_id.id,
            'date': self.date,
            'cardholder': self.cardholder,
            'code_security': self.code_security,
            'account_holder': self.account_holder,
            'number_approval': self.number_approval,
            'amount': self.amount,
            'image': self.image,
        }
        payment = self.env['sale.order.payment'].sudo().create(payment_val)
        payment.sale_id.write({
            'sale_payment_id': payment.id,
            'state': 'payment_pending',
        })
        return payment

    def print_report_voucher(self):
        return self.env.ref('custom_sale.action_sale_payment_voucher').report_action(self)
