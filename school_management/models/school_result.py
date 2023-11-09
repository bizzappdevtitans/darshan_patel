from odoo import api, fields, models


class SchoolResult(models.Model):
    _name = "school.result"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "School Result"

    # result attributes fields #T00341
    name = fields.Char(string="Student name")
    enroll_number = fields.Char(string="Enrollment No:", required=True)
    standard = fields.Integer(tracking=True)
    date_start = fields.Date(string="Result Declaration Date", required=True)
    image = fields.Image(string="MarkSheet")
    chemistry = fields.Integer(string="Chemistry Marks")
    maths = fields.Integer(string="Maths Marks")
    physics = fields.Integer(string="Physics Marks")
    university = fields.Char()
    recheck_record = fields.Char(string="Recheck Result Status")

    # compute method for finding total of given subject #T00341
    @api.depends("chemistry", "physics", "maths")
    def _compute_student_result(self):
        """this method is implement for calculate total of above three subjects #T00341"""
        for total in self:
            total.marks = (total.chemistry + total.physics + total.maths) / 3

    marks = fields.Integer(compute="_compute_student_result", search="_search_marks")

    # field search method for search view #T00436
    def _search_marks(self, operator, value):
        # this method is show that marks that have match criteria given below #T00436
        return [
            "&",
            "&",
            ("maths", ">", value),
            ("chemistry", ">", value),
            ("physics", ">", value),
        ]

    # craete inherit ORM method #T00341
    @api.model
    def create(self, values):
        """this method is implement for get default today date in result declare date
        #T00341
        """
        values["recheck_record"] = "Not applied for recheck result"
        return super(SchoolResult, self).create(values)

    # copy inherit ORM method #T00341
    def copy(self, default=None):
        """this function is implement for if duplicate the record than new record name
        will [name - COPY] formate #T00341
        """
        if default is None:
            default = {}
        if not default.get("name"):
            default["name"] = (self.name, "COPY")
        return super(SchoolResult, self).copy(default)

    # sql constraints for unique name  #T00341
    _sql_constraints = [
        (
            "student_unique_name",
            "unique (name)",
            "The name of the student mustbe unique !",
        ),
    ]

    # name_get override method #T00341
    @api.depends("name", "enroll_number")
    def name_get(self):
        """this method is for concate the name and enroll number #T00341"""
        player_list = []
        for record in self:
            player_list.append(
                (record.id, "[%s] : [%s]" % (record.name, record.enroll_number))
            )
        return player_list

    # name_search override ORM method #T00341
    @api.model
    def name_search(self, name, args=None, operator="ilike", limit=100):
        """this method is for search particular string of given records #T00341"""
        args = args or []
        if name:
            result_record = self.search(
                ["|", ("name", operator, name), ("enroll_number", operator, name)]
            )
            return result_record.name_get()
        return self.search([("name", operator, name)] + args, limit=limit).name_get()
