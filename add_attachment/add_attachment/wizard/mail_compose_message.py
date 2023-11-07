from odoo import models


class MailComposer(models.TransientModel):
    _inherit = "mail.compose.message"

    # inherit method for add attachments from chatter #T00463
    def _onchange_template_id(self, template_id, composition_mode, model, res_id):
        """this method is add auto attachment in mail from chatter #T00463"""
        values = super(MailComposer, self)._onchange_template_id(
            template_id, composition_mode, model, res_id
        )
        default_res_id = self._context.get("default_res_id")
        default_model = self._context.get("default_model")
        attachment_ids = (
            self.env["ir.attachment"]
            .search(
                [("res_id", "=", default_res_id), ("res_model", "=", default_model)]
            )
            .mapped("id")
        )
        attachment_ids.extend(values["value"].get("attachment_ids")[0][2])
        values["value"].update({"attachment_ids": [(6, 0, attachment_ids)]})
        return values
