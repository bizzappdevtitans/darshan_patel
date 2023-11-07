from odoo import models, fields, api


class BookAppointment(models.TransientModel):
    _name = "book.appointment"
    _description = "Book Appointment"

    # field for book appointment wizard #T00470
    name = fields.Char(string="Customer Name", required=True)
    mobile_number = fields.Integer(string="Mobile Number", required=True)
    customer_mail = fields.Char(string="Customer Mail", required=True)
    car_model = fields.Char(string="Car Model Name", required=True)
    car_number = fields.Char(string="Car Number", required=True)
    appointment_date = fields.Date(string="Appointment Date", required=True)
    select_service = fields.Many2many(
        comodel_name="automotive.accessories", string="Select Service", required=True
    )
    pick_up_address = fields.Char(string="Pick Up Address")
    drop_address = fields.Char(string="Drop Address")

    # method for book service appointment #T00470
    def action_book_appointment(self):
        """this methos will create new record for service appointment #T00470"""
        mechanics_vacance = self.env["automotive.mechanic"].search([])
        for mechanic in mechanics_vacance:
            if not mechanic.work_assigned:
                vals = {
                    "name": self.name,
                    "car_model": self.car_model,
                    "car_number": self.car_number,
                    "appointment_date": self.appointment_date,
                    "car_sevices_ids": self.select_service,
                    "contact_number": self.mobile_number,
                    "assigned_mechanic_id": mechanic.id,
                    "pick_up_address": self.pick_up_address,
                    "drop_address": self.drop_address,
                    "customer_mail": self.customer_mail,
                }
                self.env["service.appointment"].create(vals)
                break
