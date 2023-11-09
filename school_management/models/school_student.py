from datetime import date

from dateutil import relativedelta

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class SchoolStudent(models.Model):
    _name = "student.name"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Student Details"

    # student attributes fields #T00341
    rollno = fields.Char(string="Enrollment No", readonly=1)
    name = fields.Char(string="Student name")
    marks = fields.Float()
    university = fields.Char()
    date_of_birth = fields.Date()
    gender = fields.Selection([("Male", "Male"), ("Female", "Female")], default="Male")
    book_read_id = fields.Many2one(
        comodel_name="school.library",
        string="Book read",
    )
    phone = fields.Char(string="Mobile Number")
    standard = fields.Integer()
    admin_user_id = fields.Many2one(comodel_name="res.users", string="Admitted By")

    # compute method for calculate student age with help of date of birth #T00441
    @api.depends("date_of_birth")
    def _compute_student_age(self):
        """method is find the age of student using date od birth #T00441"""
        for record in self:
            today_date = date.today()
            record.student_age = relativedelta.relativedelta(
                today_date, record.date_of_birth
            ).years

    student_age = fields.Integer(
        string="Age",
        readonly=False,
        compute="_compute_student_age",
        inverse="_inverse_compute_method",
    )

    # inverse method for calculate date of birth with help of age #T00441
    def _inverse_compute_method(self):
        """inverse method is find the date of birth using student age #T00441"""
        for record in self:
            record.date_of_birth = date.today() - relativedelta.relativedelta(
                years=int(self.student_age)
            )

    # student state for status #T00341
    state = fields.Selection(
        [
            ("admitted", "Admitted"),
            ("study", "Study"),
            ("drop_out", "Drop Out"),
            ("passed", "Pass"),
        ],
        string="Status",
        required=True,
        default="admitted",
        tracking=True,
    )
    semester = fields.Selection(
        [
            ("SEM 1", "SEMESTER 1"),
            ("SEM 2", "SEMESTER 2"),
        ],
        string="SEMESTER",
        tracking=True,
    )

    teacher_ids = fields.Many2many(
        comodel_name="school.teacher",
        string="Teacher Name",
    )
    library_book_record_ids = fields.Many2many(
        comodel_name="school.library",
        string="Book Record",
    )
    result = fields.Selection([("Pass", "Pass"), ("Fail", "Fail")])
    remaindays = fields.Date(string="Remaining Days")

    # function for buttons for state change #T00341
    def button_study(self):
        """this button is use for change state to in study #T00341"""
        self.write({"state": "study"})

    def button_admitted(self):
        """this button is use for change state to admitted #T00341"""
        self.write({"state": "admitted"})

    def button_drop_out(self):
        """this button is use for change state to drop_out #T00341"""
        self.write({"state": "drop_out"})

    def button_passed(self):
        """this button is use for change state to passed #T00341"""
        self.write({"state": "passed"})

    student_record_count = fields.Integer(
        string="RECORDS", compute="_compute_count_records"
    )

    # search count override method for smart button #T00341
    @api.depends("name")
    def _compute_count_records(self):
        """this method is count the total name as self in records #T00341"""
        for player_record in self:
            player_record.student_record_count = self.env["school.sports"].search_count(
                [("name", "=", self.name)]
            )

    # function for domain for smart button #T00341
    def new_record_list(self):
        """this function return the domain for smart button #T00341"""
        return {
            "name": ("Student Records"),
            "res_model": "school.sports",
            "view_mode": "tree,form",
            "domain": [("name", "=", self.name)],
            "target": "current",
            "type": "ir.actions.act_window",
        }

    # unlink inherit ORM method #T00341
    def unlink(self):
        """if state is not admitted and user want to delete record than it will
        raise an error #T00341"""
        if self.state != "admitted":
            raise ValidationError(_("You can only delete record in admitted state"))
        return super(SchoolStudent, self).unlink()

    # create inherit ORM method for sequence generator #T00341
    @api.model
    def create(self, values):
        """this method is set default value for sequence after save new record
        #T00341"""
        values["rollno"] = self.env["ir.sequence"].next_by_code("student.name")
        return super(SchoolStudent, self).create(values)
