from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    sale_order_reference = fields.Char()
