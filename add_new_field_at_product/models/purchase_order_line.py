from odoo import api, fields, models


class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    short_description = fields.Char()

    @api.onchange("product_id")
    def onchange_product_id(self):
        """set field value from product template to purchase order line #T7041"""
        values = super(PurchaseOrderLine, self).onchange_product_id()
        self.short_description = self.product_id.short_description
        return values
