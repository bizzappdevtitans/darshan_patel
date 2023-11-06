from odoo import models


class MailComposer(models.TransientModel):
    _inherit = "mail.compose.message"

    # inherit method for add attachments from chatter #T00463
    def _onchange_template_id(self, template_id, composition_mode, model, res_id):
        """this method is add auto attachment in mail from chatter #T00463"""
        super(MailComposer, self)._onchange_template_id(
            template_id, composition_mode, model, res_id
        )

        default_res_id = self._context.get("default_res_id")
        default_model = self._context.get("default_model")
        attachments = self.env["ir.attachment"].search(
            [("res_id", "=", default_res_id), ("res_model", "=", default_model)]
        )
        attachment_ids = []
        for attach in attachments:
            attachment_ids.append(attach.id)

        default_values = self.with_context(
            default_composition_mode=composition_mode,
            default_model=model,
            default_res_id=res_id,
        ).default_get(
            [
                "composition_mode",
                "model",
                "res_id",
                "parent_id",
                "partner_ids",
                "subject",
                "body",
                "email_from",
                "reply_to",
                "attachment_ids",
                "mail_server_id",
            ]
        )
        values = {
            key: default_values[key]
            for key in [
                "subject",
                "body",
                "partner_ids",
                "email_from",
                "reply_to",
                "attachment_ids",
                "mail_server_id",
            ]
            if key in default_values
        }
        self.attachment_ids = [(6, 0, attachment_ids)]
        return {"value": values}
