from odoo import fields, models


class Profession(models.Model):
    _name = 'profession'
    _description = 'Profesiones'
    _rec_name = 'name'

    name = fields.Char(string="Nombre")
