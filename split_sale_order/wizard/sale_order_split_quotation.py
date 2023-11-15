from odoo import _, fields, models
from odoo.exceptions import ValidationError


class SaleOrderSplitQuotation(models.TransientModel):
    _name = "sale.order.split.quotation"
    _description = "Sale Order Split Quotation"

    # fields for Sale Order Split Quotation wizard #T00482
    sale_order_id = fields.Many2one(comodel_name="sale.order", string="Sale Order")
    split_sale_order = fields.Boolean()

    # action_split_sale_order for split sale order based on category #T00482
    def action_split_sale_order(self):
        """this method is use for create sale order if there are no
        splited sale order otherwise raise validation error #T00482"""
        if not self.sale_order_id.sale_order_reference:
            if self.split_sale_order:
                product_category = []
                for product in self.sale_order_id.order_line:
                    if product.product_id.categ_id.name not in product_category:
                        product_category.append(product.product_id.categ_id.name)

                for category in product_category:
                    product_list = [
                        product.id
                        for product in self.sale_order_id.order_line
                        if category == product.product_id.categ_id.name
                    ]

                    self.env["sale.order"].create(
                        {
                            "partner_id": self.sale_order_id.partner_id.id,
                            "sale_order_reference": self.sale_order_id.name,
                            "order_line": product_list,
                        }
                    )
            else:
                raise ValidationError(_("Please check the split sale order field"))

        else:
            raise ValidationError(_("This sale order is already splited"))
