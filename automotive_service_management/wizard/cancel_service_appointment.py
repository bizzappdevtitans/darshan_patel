from odoo import models, fields, api


class CancelAppointment(models.Model):
    _name = 'cancel.appointment'
    _description = 'cancel.appointment'

    appointment_ids = fields.Many2one(string="Select Appointment", comodel_name="service.appointment")

    def action_cancel_service_appointment(self):
        self.appointment_ids.unlink()
