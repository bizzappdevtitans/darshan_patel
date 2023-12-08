from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    short_description = fields.Char(
        compute="_compute_short_description",
        inverse="_inverse_short_description",
        readonly=False,
        store=True,
    )

    @api.depends("product_variant_ids.short_description")
    def _compute_short_description(self):
        """compute method for set value in product template #T7041"""
        for template in self:
            template.short_description = template.product_variant_ids.short_description

    def _inverse_short_description(self):
        """inverse method for set value in product variants #T7041"""
        self.product_variant_ids.short_description = self.short_description
