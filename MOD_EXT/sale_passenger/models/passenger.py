from odoo import fields, models, api


class Passenger(models.Model):
    _name = 'passenger'
    _description = 'Pasajeros'
    _rec_name = 'name'

    name = fields.Char(index=True)
    doc_type = fields.Selection([('v', 'V'), ('e', 'E'), ('j', 'J'), ('g', 'G'), ('p', 'P'), ('c', 'C')],
                                required=True, default='v')
    nationality_id = fields.Many2one('res.country', string="Nacionalidad")
    country_id = fields.Many2one('res.country', string='Country', ondelete='restrict')
    gender = fields.Selection(string="Genero", selection=[('F', 'Femenino'), ('M', 'Masculino'), ('other', 'Otros')])
    vat = fields.Char(string="Cedula")
    image_128 = fields.Image("Image 128", max_width=128, max_height=128, store=True)
    street = fields.Char()
    street2 = fields.Char()
    zip = fields.Char(change_default=True)
    city = fields.Char()
    email = fields.Char()
    phone = fields.Char()
    mobile = fields.Char()
    state_id = fields.Many2one("res.country.state", string='State', ondelete='restrict',
                               domain="[('country_id', '=?', country_id)]")
    partner_id = fields.Many2one('res.partner', string="Cliente")
