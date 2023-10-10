from odoo import fields, models, api


class SaleOrder(models.Model):
    _inherit = "sale.order"

    partner_id = fields.Many2one(comodel_name="res.partner")

    @api.depends('partner_id')
    def onchange_user_id(self):

        print("onchange_partner_id method called")

        return super(SaleOrder, self).onchange_user_id()
