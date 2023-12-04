from odoo import _, fields, models
from odoo.exceptions import ValidationError


class SaleOrderSplitQuotation(models.TransientModel):
    _name = "sale.order.split.quotation"
    _description = "Sale Order Split Quotation"

    # fields for Sale Order Split Quotation wizard #T6982
    split_sale_order = fields.Selection(
        [
            ("based_on_category", "Based on category"),
            ("selected_lines", "Selected Lines"),
            ("one_line_per_order", "One Line Per Order"),
        ],
        string="split sale order",
    )
    sale_order_line_ids = fields.Many2many(comodel_name="sale.order.line")

    # action_split_sale_order for split sale order based on split sale order #T6982
    def action_split_sale_order(self):
        """this method is use for split sale order #T6982"""
        sale_order = self._context.get("active_ids", [])
        sale_order_id = self.env["sale.order"].search([("id", "=", sale_order)])

        # for split_sale_order is based on category than this function will split
        # sale order based on category #T6982
        if self.split_sale_order == "based_on_category":
            # this method split sale order based on category #T6982
            if not sale_order_id.sale_order_reference:
                if self.split_sale_order:
                    product_category = []
                    for product in sale_order_id.order_line:
                        if product.product_id.categ_id.name not in product_category:
                            product_category.append(product.product_id.categ_id.name)

                    for category in product_category:
                        product_list = [
                            product.id
                            for product in sale_order_id.order_line
                            if category == product.product_id.categ_id.name
                        ]

                        self.env["sale.order"].create(
                            {
                                "partner_id": sale_order_id.partner_id.id,
                                "sale_order_reference": sale_order_id.name,
                                "order_line": product_list,
                            }
                        )
                else:
                    raise ValidationError(_("Please check the split sale order field"))

            else:
                raise ValidationError(_("This sale order is already splited"))

        # for split_sale_order is selected line than it will create sale order of
        # selected product #T6982
        elif self.split_sale_order == "selected_lines":
            # this method create sale order on selected product #T6982
            if not sale_order_id.sale_order_reference:
                for product in self.sale_order_line_ids:
                    selected_product_list = [
                        product.id for product in self.sale_order_line_ids
                    ]
                    self.env["sale.order"].create(
                        {
                            "partner_id": sale_order_id.partner_id.id,
                            "sale_order_reference": sale_order_id.name,
                            "order_line": selected_product_list,
                        }
                    )
                    break
            else:
                raise ValidationError(_("This sale order is already splited"))

        # for split_sale_order is one line  per order than this function is create new
        # sale order for each product in sale order #T6982
        elif self.split_sale_order == "one_line_per_order":
            if not sale_order_id.sale_order_reference:
                for product in sale_order_id.order_line:
                    self.env["sale.order"].create(
                        {
                            "partner_id": sale_order_id.partner_id.id,
                            "sale_order_reference": sale_order_id.name,
                            "order_line": product,
                        }
                    )
            else:
                raise ValidationError(_("This sale order is already splited"))
