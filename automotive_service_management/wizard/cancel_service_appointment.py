from odoo import models, fields, api
from odoo.exceptions import ValidationError


class CancelAppointment(models.TransientModel):
    _name = "cancel.appointment"
    _description = "cancel.appointment"

    appointment_ids = fields.Many2one(
        string="Select Appointment", comodel_name="service.appointment"
    )

    def action_cancel_service_appointment(self):
        if self.appointment_ids.state == "appointed":
            self.appointment_ids.unlink()
        else:
            raise ValidationError(
                f"In {self.appointment_ids.state} State You can Not Cancel Appointment"
            )
