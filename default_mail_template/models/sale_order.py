from odoo import models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def action_quotation_send(self):
        """Inherit method for set default mail template in send mail wizard"""
        val = super(SaleOrder, self).action_quotation_send()
        default_template = self.env.company.default_so_mail_template.id
        context = val["context"]
        # update default_template_id in context #T7012
        context.update({"default_template_id": default_template})
        return val
