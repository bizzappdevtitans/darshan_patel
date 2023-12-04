from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    # field for set main sale order number #T6982
    sale_order_reference = fields.Char(readonly=True)
