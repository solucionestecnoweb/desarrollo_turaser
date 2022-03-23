# -*- coding: utf-8 -*-

from odoo import fields, models


class CountryState(models.Model):
    """ Add Municipalities reference in State """
    _name = 'res.country.state'
    _inherit = 'res.country.state'
    _description = "Country states"

    municipality_ids = fields.One2many('res.country.state.municipality', 'state_id', 'Municipalities in this state')
    ubigeo = fields.Char(string='ubigeo code', size=2)


class StateMunicipality(models.Model):
    """States Municipalities"""
    _name = 'res.country.state.municipality'
    _description = "State municipalities"

    state_id = fields.Many2one('res.country.state', 'State', required=True,
                               help='Name of the State to which the municipality belongs')
    name = fields.Char('Municipality', required=True, help='Municipality name')
    parish_ids = fields.One2many('res.country.state.municipality.parish', 'municipality_id',
                                 help='Parishes in this municipality')
    ubigeo = fields.Char(string='ubigeo code', size=4)


class MunicipalityParish(models.Model):
    """States Parishes"""
    _name = 'res.country.state.municipality.parish'
    _description = "Municipality parishes"

    municipality_id = fields.Many2one('res.country.state.municipality', 'Municipality',
                                      help='Name of the Municipality to which the parish belongs')
    name = fields.Char('Parish', required=True, help='Parish name')
    ubigeo = fields.Char(string='ubigeo code', size=6)