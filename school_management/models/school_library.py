from datetime import date

from dateutil import relativedelta

from odoo import api, fields, models


class SchoolLibrary(models.Model):
    _name = "school.library"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "School Library"

    # book attributes fields #T00341
    code = fields.Integer(string="Book Code", required=True)
    name = fields.Char(string="Book Name")
    book_author = fields.Char()
    sports_player_record_ids = fields.Many2many(
        comodel_name="school.sports",
        string="Player Record",
    )
    book_price = fields.Integer()

    # field for book is allocated to which person #T00341
    allocated_person = fields.Reference(
        selection=[
            ("school.sports", "School Sports"),
            ("student.name", "Student Record"),
            ("school.teacher", "Teacher Record"),
        ],
    )

    book_issue_date = fields.Date(readonly=True)
    book_return_date = fields.Date()

    # create inherit ORM method for book_issue_date and calculate book_return_date #T00353
    @api.model
    def create(self, values):
        """this method is implement for get default today date and calculate as per
        parameter date in book_return_date #T00353"""
        book_issue_duration = self.env["ir.config_parameter"].get_param(
            "school_management.book_issue_duration"
        )
        values["book_issue_date"] = date.today()
        values["book_return_date"] = date.today() + relativedelta.relativedelta(
            months=int(book_issue_duration)
        )
        return super(SchoolLibrary, self).create(values)
