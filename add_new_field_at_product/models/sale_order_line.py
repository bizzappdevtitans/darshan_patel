from odoo import fields, models


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    short_description = fields.Char(related="product_id.short_description")
