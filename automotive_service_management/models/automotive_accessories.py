from odoo import models, fields


class AutomotiveAccessories(models.Model):
    _name = 'automotive.accessories'
    _description = 'automotive.accessories'
    _inherit = ['image.mixin']

    name = fields.Char(string="Service Name")
    service_charge = fields.Integer(string='Service Charge')
    accessories_name = fields.Char(string="Accessories Name")
    image_256 = fields.Image(string="Accessories Image", readonly=False, max_width=256, max_height=256)
