from odoo import fields, models


class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    short_description = fields.Char(related="product_id.short_description")
