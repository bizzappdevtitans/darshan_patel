from odoo import models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def action_quotation_send(self):
        """Inherit method for set default mail template in send mail wizard"""
        val = super(SaleOrder, self).action_quotation_send()
        template_id = self.env.company.default_so_mail_template.id
        context = val["context"]
        # update default_template_id in context #T7012
        context.update({"default_template_id": template_id})
        return val
