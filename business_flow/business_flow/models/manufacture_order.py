from odoo import fields, models


class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    # manufacturing order field #T00405
    manufacturing_description = fields.Char(string='Manufacturing Description')
