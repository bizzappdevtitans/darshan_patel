from odoo import models, fields, api


class BookAppointment(models.Model):
    _name = 'book.appointment'
    _description = 'book.appointment'

    name = fields.Char(string="Customer Name", required=True)
    car_model = fields.Char(string="Car Model Name", required=True)
    car_number = fields.Char(string="Car Number", required=True)
    appointment_date = fields.Date(string="Appointment Date", required=True)
    select_service = fields.Many2many(comodel_name="automotive.accessories", string="Select Service")

    def action_book_appointment(self):
        mechanics_vacance = self.env['automotive.mechanic'].search([])
        for mechanic in mechanics_vacance:
            if not mechanic.work_assigned:
                vals = {
                    "name": self.name,
                    "car_model": self.car_model,
                    "car_number": self.car_number,
                    "appointment_date": self.appointment_date,
                    "car_sevices_ids": self.select_service,
                    "assigned_mechanic": mechanic.id
                }
                mechanic.write({'work_assigned': 'True'})
                self.env['service.appointment'].create(vals)
                break
