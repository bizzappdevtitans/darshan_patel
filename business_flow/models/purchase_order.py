from odoo import fields, models


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    # purchase order field #T00388
    purchase_description = fields.Char()
