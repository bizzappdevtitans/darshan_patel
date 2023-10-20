from odoo import models, fields


class AutomotiveAccessories(models.Model):
    _name = 'automotive.accessories'
    _description = 'automotive.accessories'

    name = fields.Char(string="Service Name")
    service_charge = fields.Integer(string='Service Charge')
    accessories_name = fields.Char(string="Accessories Name")
