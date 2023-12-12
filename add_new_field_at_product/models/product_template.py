from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    short_description = fields.Char(
        compute="_compute_short_description",
        inverse="_inverse_short_description",
    )

    @api.depends("product_variant_ids.short_description")
    def _compute_short_description(self):
        """compute method for set value in product template #T7041"""
        for template in self:
            variant_count = len(template.product_variant_ids)
            if variant_count > 1:
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

    @api.model_create_multi
    def create(self, vals_list):
        """create method for set short description value #T7041"""
        templates = super(ProductTemplate, self).create(vals_list)
        for template, vals in zip(templates, vals_list):
            related_vals = {}
            if vals.get("short_description"):
                # get the value of short_description into related_vals #T7041
                related_vals["short_description"] = vals["short_description"]
            if related_vals:
                # pass short_description value to the template #T7041
                template.write(related_vals)
        return templates
