# -*- coding: utf-8 -*-

from odoo import fields, models, api


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

    pnr = fields.Char(string="PNR", copy=False)
    product_location_in = fields.Char(string='localizador Interno', copy=False)
    is_service = fields.Boolean(string="Extension de Servicio", copy=False)
    parent_id = fields.Many2one('sale.order', string="Documento origen", copy=False)
    seller_id = fields.Many2one('res.partner', string="Enterado por")
    sale_payment_id = fields.Many2one('sale.order.payment', string="Pago", copy=False)
    promotion_id = fields.Many2one('promotion', string="Promocion", copy=False)
    number_promotion = fields.Char(string="Nro. de Promocion", copy=False)
    state = fields.Selection([
        ('draft', 'Quotation'),
        ('sent', 'Quotation Sent'),
        ('pre_confirm', 'Cotización de Servicio Pre-Confirmada'),
        ('sale', 'Sales Order'),
        ('service_for_approved', 'Servicio por Aprobar'),
        ('service_approved', 'Servicio Aprobado'),
        ('service_issue_voucher', 'Servicio por Emitir Voucher'),
        ('voucher_issue', 'Voucher Liberado'),
        ('voucher_issue_send', 'Voucher enviado por correo electronico o whatsapp'),
        ('pre_invoice', 'Pre-Factura'),
        ('invoice', 'Factura'),
        ('done', 'Locked'),
        ('cancel', 'Cancelled'),
        ], string='Status', readonly=True, copy=False, index=True, tracking=3, default='draft')

    @api.model
    def create(self, vals):
        """
        This method is create for sequence wise name.
        :param vals: values
        :return:super
        """
        res = super(SaleOrder, self).create(vals)
        res.product_location_in = self.env['ir.sequence'].next_by_code('sale.order.location')
        return res

    def action_pre_confirm(self):
        self.write({'state': 'pre_confirm'})

    def action_voucher_issue(self):
        self.write({'state': 'service_issue_voucher'})

    def action_validate_voucher(self):
        self.write({'state': 'voucher_issue'})
        for sale in self.order_line:
            if sale.type_service in ['hotel', 'transfer']:
                return self.env.ref('custom_sale.action_sale_voucher').report_action(self)

    def action_validate_pre_factura(self):
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

    def action_sale_payment(self):
        return {
            'res_model': 'sale.order.payment',
            'view_mode': 'form',
            'res_id': self.sale_payment_id.id,
            'target': 'current',
            'type': 'ir.actions.act_window',
        }

    def _find_mail_template(self, force_confirmation_template=False):
        template_id = False
        if force_confirmation_template or (self.state == 'voucher_issue'):
            if not template_id:
                template_id = self.env['ir.model.data'].xmlid_to_res_id('sale.mail_template_sale_confirmation', raise_if_not_found=False)
                return template_id

    def action_quotation_voucher_send(self):
        self.ensure_one()
        # template_id = self._find_mail_template()
        # lang = self.env.context.get('lang')
        # template = self.env['mail.template'].browse(template_id)
        # if template.lang:
        #     lang = template._render_lang(self.ids)[self.id]
        # ctx = {
        #     'default_model': 'sale.order',
        #     'default_res_id': self.ids[0],
        #     'default_use_template': bool(template_id),
        #     'default_template_id': template_id,
        #     'default_composition_mode': 'comment',
        #     'mark_so_as_sent': True,
        #     'custom_layout': "mail.mail_notification_paynow",
        #     'proforma': self.env.context.get('proforma', False),
        #     'force_email': True,
        #     'model_description': self.with_context(lang=lang).type_name,
        # }
        return {
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'mail.compose.message',
            'views': [(False, 'form')],
            'view_id': False,
            'target': 'new',
            # 'context': ctx,
        }

