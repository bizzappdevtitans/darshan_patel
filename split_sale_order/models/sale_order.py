from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    # field for set main sale order number #T6982
    sale_order_reference = fields.Char(readonly=True)

    def copy(self, default=None):
        """Added copy method for set default single space on copied splited sale
        order #T6982"""
        default = dict(default or {})
        default["sale_order_reference"] = " "
        return super(SaleOrder, self).copy(default=default)
