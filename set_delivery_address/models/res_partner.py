from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    type = fields.Selection(selection_add=[('drop_shipping_address', 'Drop Shipping Address')])
    address_verified = fields.Boolean(string='Address Verified')
