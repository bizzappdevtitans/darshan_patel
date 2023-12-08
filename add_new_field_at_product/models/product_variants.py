from odoo import fields, models


class ProductVariants(models.Model):
    _inherit = "product.product"

    short_description = fields.Char()
