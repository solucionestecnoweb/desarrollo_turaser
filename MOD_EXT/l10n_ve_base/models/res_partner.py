# -*- coding: utf-8 -*-

from odoo import fields, models, api


class Partner(models.Model):
    _inherit = 'res.partner'

    vat2 = fields.Char(string="Cedula")
    birth_date = fields.Date(string="Fecha de Nacimiento/Aniversario")
    gender = fields.Selection(string="Genero", selection=[('F', 'Femenino'), ('M', 'Masculino'), ('other', 'Otros')])
    nationality_id = fields.Many2one('res.country', string="Nacionalidad")
    company_type = fields.Selection(selection_add=[('freelance', 'Freelance')])
    is_freelance = fields.Boolean(string='Is freelance', default=False)

    @api.depends('is_company', 'is_freelance')
    def _compute_company_type(self):
        for partner in self:
            if partner.is_freelance:
                partner.company_type = 'freelance'
            elif partner.is_company:
                partner.company_type = 'company'
            else:
                partner.company_type = 'person'

    def _write_company_type(self):
        for partner in self:
            if partner.company_type == 'freelance':
                partner.is_freelance = partner.company_type
            elif partner.company_type == 'company':
                partner.is_company = partner.company_type
            else:
                partner.company_type = 'person'

    @api.onchange('company_type')
    def onchange_company_type(self):
        for partner in self:
            if partner.company_type == 'freelance':
                partner.is_freelance = (partner.company_type == 'freelance')
            elif partner.company_type == 'company':
                partner.is_company = (partner.company_type == 'company')
            else:
                partner.company_type = 'person'
