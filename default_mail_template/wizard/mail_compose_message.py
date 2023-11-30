from odoo import api, models


class MailComposer(models.TransientModel):
    _inherit = "mail.compose.message"

    @api.model
    # default_get method for get default mail template #T7012
    def default_get(self, fields):
        """This method is use for get default mail template that is selected
        in res.company #T7012"""
        default_template = super(MailComposer, self).default_get(fields)
        if self.env.company.default_so_mail_template:
            default_template[
                "template_id"
            ] = self.env.company.default_so_mail_template.id
        return default_template
