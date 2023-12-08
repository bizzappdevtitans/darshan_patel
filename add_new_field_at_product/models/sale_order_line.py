from odoo import api, fields, models


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    short_description = fields.Char()

    @api.onchange("product_id")
    def product_id_change(self):
        """set value from product template to sale order line #T7041"""
        values = super(SaleOrderLine, self).product_id_change()
        self.short_description = self.product_id.short_description
        return values
