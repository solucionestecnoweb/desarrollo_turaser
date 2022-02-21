from odoo import api, fields, models

class HideMenuTemplate(models.Model):
    _name = 'sh.hide.menu.template'

    name = fields.Char(String = "Name",required=True)
    menu_ids = fields.Many2many('ir.ui.menu',string = "Menus",required=True)