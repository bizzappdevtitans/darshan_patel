from odoo import fields, models


class InvoiceInherit(models.Model):
    _inherit = "account.move"

    # fields for invoice #T00375
    invoice_description = fields.Char()
    delivery_description = fields.Char()
