from odoo import fields, models


class StockPicking(models.Model):
    _inherit = "stock.picking"

    # delivery order field #T00400
    delivery_description = fields.Char(string="Delivery description")
