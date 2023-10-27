from odoo import models, fields, api
from odoo.exceptions import ValidationError


class ServicePayment(models.TransientModel):
    _name = "service.payment"
    _description = "service.payment"

    appointment_id = fields.Many2one(
        comodel_name="service.appointment", string="Appointment"
    )
    serviced_amount = fields.Integer(string="Total Amount")
    payment_mode = fields.Selection(
        [("upi", "UPI"), ("bank_account", "Bank Account")], default="upi"
    )
    upi_number = fields.Char(string="UPI ID", readonly=True)
    ifsc_code = fields.Char(string="IFSC CODE", readonly=True)
    account_number = fields.Char(string="Account Number", readonly=True)
    payment_reference_number = fields.Char(
        string="Payment Reference Number", required=True
    )

    @api.onchange("appointment_id")
    def get_amount(self):
        for record in self:
            record.update({"serviced_amount": self.appointment_id.total_cost})
            record.update(
                {
                    "upi_number": self.env["ir.config_parameter"].get_param(
                        "automotive_service_management.upi_number"
                    )
                }
            )
            record.update(
                {
                    "ifsc_code": self.env["ir.config_parameter"].get_param(
                        "automotive_service_management.ifsc_code"
                    )
                }
            )
            record.update(
                {
                    "account_number": self.env["ir.config_parameter"].get_param(
                        "automotive_service_management.account_number"
                    )
                }
            )

    def action_payment_done(self):
        for record in self.appointment_id:
            if record.state == "serviced":
                record.write({"state": "payment_done"})
                record.write(
                    {
                        "payment_reference_number": self.payment_reference_number
                        + " - "
                        + self.payment_mode
                    }
                )
            return {
                "effect": {
                    "fadeout": "slow",
                    "message": "Your Payment Has Been Done",
                    "type": "rainbow_man",
                    "img_url": "automotive_service_management/static/img/payment.png",
                }
            }
