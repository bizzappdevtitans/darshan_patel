from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    # inherited field for sale order #T00457
    type = fields.Selection(
        selection_add=[("drop_shipping_address", "Drop Shipping Address")]
    )
    address_verified = fields.Boolean()
