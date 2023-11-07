from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class SchoolTeacher(models.Model):
    _name = "school.teacher"
    _description = "School Teacher"

    # teacher attributes #T00341
    name = fields.Char(string="Teacher Name")
    subject = fields.Char()
    student_ids = fields.Many2many(
        comodel_name="student.name",
        string="Student",
    )
    teacher_ids = fields.Many2many(
        comodel_name="ir.attachment",
        string="Teacher Id",
    )
    teacher_phone = fields.Char(
        string="Phone",
    )
    teacher_mail = fields.Char(
        string="Mail",
    )
    school_name = fields.Char()
    rate = fields.Selection(
        [
            ("0", "Very Low"),
            ("1", "Low"),
            ("2", "Normal"),
            ("3", "High"),
            ("4", "Very High"),
        ]
    )

    # fields for display monetary widget #T00341
    company_id = fields.Many2one(
        comodel_name="res.company",
        store=True,
        string="Company",
        default=lambda self: self.env.user.company_id.id,
    )
    # fields for display monetary widget #T00341
    currency_id = fields.Many2one(
        comodel_name="res.currency",
        string="Currency",
        related="company_id.currency_id",
        default=lambda self: self.env.user.company_id.currency_id,
    )
    fee = fields.Monetary()

    # api.constrains for validation of mobile number #T00341
    @api.constrains("teacher_phone")
    def phone_validation(self):
        """this function check if mobile number length not equal to 10 than raise error
        #T00341"""
        for teacher_record in self:
            if teacher_record.teacher_phone and len(teacher_record.teacher_phone) != 10:
                raise ValidationError(_("Enter valid mobile number"))
        return True
