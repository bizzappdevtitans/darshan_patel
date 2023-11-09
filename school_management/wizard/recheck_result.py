from datetime import date

from dateutil import relativedelta

from odoo import fields, models
from odoo.exceptions import ValidationError


class RecheckResult(models.TransientModel):
    _name = "recheck.result"
    _description = "Recheck Result"

    # field for enroll number of student #T00365
    enrollment_number_id = fields.Many2one(
        comodel_name="school.result", string="Enrollment Number"
    )

    # system parameter for check result are eligible for recheck or not #T00365
    def action_recheck(self):
        """this function is check result declare date + given days after that any
        student are not eligible for recheck result #T00365"""
        result_recheck_duration = self.env["ir.config_parameter"].get_param(
            "school_management.result_recheck_duration"
        )

        allowed_date = (
            self.enrollment_number_id.date_start
            + relativedelta.relativedelta(days=int(result_recheck_duration))
        )
        if allowed_date < date.today():
            raise ValidationError(
                f"You Can Only Recheck the result within {result_recheck_duration} days"
            )
        # write method for print the name that who apply recheck result #T00365
        self.enrollment_number_id.write(
            {
                "recheck_record": self.enrollment_number_id.name
                + " Is Applied For Recheck Result"
            }
        )
