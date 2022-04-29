# -*- coding: utf-8 -*-

from odoo import fields, models, api


class SaleOrderPayment(models.Model):
    _name = 'sale.order.payment'
    _description = 'Pagos Ventas'
    _rec_name = 'name'

    name = fields.Char(string='Numero de pago',  copy=False)
    partner_id = fields.Many2one('res.partner', string='Cliente')
    sale_id = fields.Many2one('sale.order', string='Pedido de Venta')
    card_type_id = fields.Many2one('sale.order.card.type', string='Tipo de Tarjeta')
    bank_id = fields.Many2one('sale.order.bank', string='Banco')
    payment_method_id = fields.Many2one('sale.order.payment.method', string='Metodo de Pago')
    vat2 = fields.Char(related='partner_id.vat2', string='Numero de Cedula')
    passport_ids = fields.One2many('passport', related='partner_id.passport_ids', string='Pasaporte', readonly=False)
    date = fields.Date(string='Fecha')
    cardholder = fields.Char(string='Tarjetahabiente')
    code_security = fields.Char(string='Codigo de Seguridad')
    account_holder = fields.Char(string='Titular de Cuenta')
    number_approval = fields.Char(string='Numero de aprobacion')
    amount = fields.Float(string='Monto')
    image = fields.Binary(string='imagen', store=True, attachment=True)
    state = fields.Selection([('draft', 'Borrador'), ('confirmed', 'Pago confimardo'), ('cancel', 'Cancelado')],
                             string='Status', readonly=True, copy=False, index=True, tracking=3, default='draft')
    serial = fields.Text(string='Seriales')

    @api.model
    def create(self, vals):
        """
        This method is create for sequence wise name.
        :param vals: values
        :return:super
        """
        res = super(SaleOrderPayment, self).create(vals)
        res.name = self.env['ir.sequence'].next_by_code('sale.order.payment')
        return res

    def action_payment_for_approval(self):
        self.write({'state': 'confirmed'})
        self.sale_id.write({'state': 'service_for_approved'})

    def action_cancel(self):
        self.write({'state': 'cancel'})


class SaleOrderPaymentMethod(models.Model):
    _name = 'sale.order.payment.method'
    _description = 'Metodos de Pagos Ventas'

    name = fields.Char(string="Nombre")
    active = fields.Boolean(string="Activo")



