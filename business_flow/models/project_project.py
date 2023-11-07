from odoo import fields, models


class Project(models.Model):
    _inherit = "project.project"

    # fields for project #T00384
    project_description = fields.Char()
