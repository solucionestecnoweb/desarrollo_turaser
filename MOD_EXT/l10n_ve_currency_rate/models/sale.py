from datetime import datetime
from dateutil.relativedelta import relativedelta

from odoo import api, fields, models, SUPERUSER_ID, _
from odoo.osv import expression
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT
from odoo.tools.float_utils import float_compare
from odoo.exceptions import AccessError, UserError, ValidationError
from odoo.tools.misc import formatLang, get_lang


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    custom_rate = fields.Boolean(string='¿Usar tasa de cambio personalizada?')
    rate = fields.Float(string='Tasa', default=lambda x: x.env['res.currency.rate'].search([
        ('name', '<=', fields.Date.today()), ('currency_id', '=', 2)], limit=1).sell_rate, digits=(12, 2))
    usd_currency_id = fields.Many2one(comodel_name='res.currency', string='USD Currency', default=2)
    amount_total_usd = fields.Monetary(string=' Total $')
    amount_untaxed_usd = fields.Monetary(string=' Total libre de impuestos $')

    def _create_invoices(self, grouped=False, final=False):
        invoice = super(SaleOrder, self)._create_invoices(grouped, final)
        invoice['custom_rate'] = True
        invoice['os_currency_rate'] = self.rate
        return invoice
    
    @api.onchange('amount_untaxed','amount_total')
    def onchange_total_usd(self):
        for item in self:
            item._compute_total_usd()
    
    @api.constrains('amount_untaxed', 'amount_total')
    def constrains_total_usd(self):
        for item in self:
            item._compute_total_usd()


    @api.onchange('pricelist_id')
    def onchange_pricelist(self):
        self.rate = self.pricelist_id.rate

    @api.onchange('rate', 'order_line')
    def onchange_price(self):
        for item in self.order_line:
            item.price_unit = item.product_id.list_price_usd * self.rate
    
    def _compute_total_usd(self):
        for item in self.env['sale.order'].search([]):
            if item.rate:
                item.amount_total_usd = item.amount_total / item.rate
                item.amount_untaxed_usd = item.amount_untaxed / item.rate
            else:
                item.amount_total_usd = 0


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    price_unit_usd = fields.Float(string='Precio unidad $', related='product_id.list_price_usd')
    price_total_usd = fields.Float(string='Precio total $')

    @api.constrains('price_total')
    def set_price_total_usd(self):
        self.price_total_usd = self.price_total / self.order_id.rate


class SaleReport(models.Model):
    _inherit = 'sale.report'

    price_total_usd = fields.Float(string='Total $')
    amount_untaxed_usd = fields.Float(string='Libre de Impuesto $')
    rate = fields.Float(string='tipo de cambion')
    
    price_total_usd = fields.Float(compute='_compute_price_total_usd', string='Total $',store=True)
    
    def _compute_price_total_usd(self):
        for item in self:
            if item.rate > 1:
                item.price_total_usd = item.price_total / item.rate
            else : 
                item.price_total_usd = item.price_total 

    def _query(self, with_clause='', fields={}, groupby='', from_clause=''):
       
        fields['price_total_usd'] = ", CASE WHEN s.rate > 0 THEN sum(l.price_total / s.rate)  ELSE l.price_total END as price_total_usd"
        fields['amount_untaxed_usd'] = ", s.amount_untaxed_usd  as amount_untaxed_usd "
        fields['rate'] = ", s.rate  as rate "
        
        groupby += ', l.price_total'
        groupby += ', s.amount_untaxed_usd'
        groupby += ', s.rate'
        return super(SaleReport, self)._query(with_clause, fields, groupby, from_clause)
