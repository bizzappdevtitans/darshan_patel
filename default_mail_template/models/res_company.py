from odoo import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    # field for select default mail template in company #T7012
    default_so_mail_template = fields.Many2one(
        comodel_name="mail.template", domain="[('model_id', '=', 'sale.order')]"
    )
