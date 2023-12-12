from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    short_description = fields.Char(
        compute="_compute_short_description",
        inverse="_inverse_short_description",
        readonly=False,
    )

    @api.depends("product_variant_ids.short_description")
    def _compute_short_description(self):
        """compute method for set value in product template #T7041"""
        for template in self:
            if len(template.attribute_line_ids) > 0:
                # added if statement for product variants pass field value #T7041
                for variant in template.product_variant_ids:
                    template.short_description = variant.short_description
            else:
                template.short_description = (
                    template.product_variant_ids.short_description
                )

    def _inverse_short_description(self):
        """inverse method for set value in product variants #T7041"""
        self.product_variant_ids.short_description = self.short_description
