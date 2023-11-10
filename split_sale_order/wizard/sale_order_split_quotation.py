from odoo import _, fields, models
from odoo.exceptions import ValidationError


class SaleOrderSplitQuotation(models.TransientModel):
    _name = "sale.order.split.quotation"
    _description = "Sale Order Split Quotation"

    sale_order_id = fields.Many2one(comodel_name="sale.order", string="Sale Order")
    split_sale_order = fields.Boolean()

    def action_split_sale_order(self):
        if self.split_sale_order:
            products_name = {}
            product_category = []
            for product in self.sale_order_id.order_line:
                products_name.update(
                    {product.product_id.id: product.product_id.categ_id.name}
                )
            for product in self.sale_order_id.order_line:
                if product.product_id.categ_id.name not in product_category:
                    product_category.append(product.product_id.categ_id.name)

            for category in product_category:
                for products in products_name.values():
                    if category == products:
                        product_id = (
                            self.env["product.product"]
                            .search([("id", "in", products_name)])
                            .ids
                        )
                        self.env["sale.order"].create(
                            {
                                "partner_id": self.sale_order_id.partner_id.id,
                                "order_line": [
                                    (
                                        0,
                                        0,
                                        {
                                            "product_id": product_id.id,
                                            "product_uom_qty": 1,
                                            "price_unit": 0,
                                            "tax_id": False,
                                        },
                                    )
                                ],
                            }
                        )
        else:
            raise ValidationError(_("Please check the split sale order field"))
