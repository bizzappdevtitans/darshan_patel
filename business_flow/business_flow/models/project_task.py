from odoo import fields, models


class ProjectTask(models.Model):
    _inherit = "project.task"

    # fields for pass field value for task #T00384
    task_description = fields.Char(string="Task Description")
