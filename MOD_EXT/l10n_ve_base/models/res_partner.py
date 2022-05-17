# -*- coding: utf-8 -*-

from odoo import fields, models, api


class Partner(models.Model):
    _inherit = 'res.partner'

    vat2 = fields.Char(string="Cedula")
    birth_date = fields.Date(string="Fecha de Nacimiento/Aniversario")
    gender = fields.Selection(string="Genero", selection=[('F', 'Femenino'), ('M', 'Masculino'), ('other', 'Otros')])
    nationality_id = fields.Many2one('res.country', string="Nacionalidad")
    is_nationality_two = fields.Boolean(string='Tiene segunda nacionalidad?', default=False)
    nationality_id2 = fields.Many2one('res.country', string="Segunda Nacionalidad")
    company_type = fields.Selection(selection_add=[('freelance', 'Freelance')])
    is_freelance = fields.Boolean(string='Is freelance', default=False)
    doc_type = fields.Selection([('j', 'J')], required=True, default='j')
    doc_type2 = fields.Selection([('v', 'V'), ('e', 'E'), ('j', 'J'), ('g', 'G'), ('p', 'P'), ('c', 'C')],
                                 required=True, default='v')
    people_type = fields.Selection([
        ('na', 'N/A'),
        ('resident_nat_people', 'PNRE Residente Natural Person'),
        ('non_resit_nat_people', 'PNNR Non-resident Natural Person'),
        ('domi_ledal_entity', 'PJDO Domiciled Legal Entity'),
        ('legal_ent_not_domicilied', 'PJDO Legal Entity Not Domiciled')],
        string='People type', required="True", default='na')

    description_hotel = fields.Text(string="Descripcion del hotel")
    description_rates = fields.Text(string="Notificaciones y tarifas")
    policy_legal_notice = fields.Text(string="politica y aviso legal")
    email1 = fields.Char(string="Correo electronico solicitud 1")
    email2 = fields.Char(string="Correo electronico solicitud 2")
    email3 = fields.Char(string="Correo electronico solicitud 3")
    email4 = fields.Char(string="Correo electronico solicitud 4")

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
        for partner1 in self:
            if partner1.company_type == 'freelance':
                partner1.is_freelance = partner1.company_type
            elif partner1.company_type == 'company':
                partner1.is_company = partner1.company_type
            else:
                partner1.company_type = 'person'

    @api.onchange('company_type')
    def onchange_company_type(self):
        for partner in self:
            if partner.company_type == 'freelance':
                partner.is_freelance = (partner.company_type == 'freelance')
            elif partner.company_type == 'company':
                partner.is_company = (partner.company_type == 'company')
            else:
                partner.company_type = 'person'
