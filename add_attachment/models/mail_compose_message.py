from odoo import models, api


class MailComposer(models.TransientModel):
    _inherit = "mail.compose.message"

    def _onchange_template_id(self, template_id, composition_mode, model, res_id):
        return super(MailComposer, self)._onchange_template_id(template_id, composition_mode, model, res_id)
