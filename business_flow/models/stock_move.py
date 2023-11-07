from odoo import models


class StockMove(models.Model):
    _inherit = "stock.move"

    # method for passing value from sale order to delivery order #T00400
    def _get_new_picking_values(self):
        """this method is used to pass field value from sale order to Delivery order #T00400"""
        delivery_values = super(StockMove, self)._get_new_picking_values()
        delivery_values[
            "delivery_description"
        ] = self.group_id.sale_id.delivery_description
        return delivery_values

    # this inherit method is use for pass field value from sale order to stock #T00388
    def _prepare_procurement_values(self):
        """this method is take value from sale and pass to stock #T00388"""
        res = super(StockMove, self)._prepare_procurement_values()
        res["purchase_description"] = self.group_id.sale_id
        res[
            "manufacturing_description"
        ] = self.sale_line_id.order_id.manufacturing_description
        return res
