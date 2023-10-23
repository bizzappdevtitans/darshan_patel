from odoo import models, fields


class AutomotiveMechanic(models.Model):
    _name = 'automotive.mechanic'
    _description = 'automotive.mechanic'

    name = fields.Char(string="Mechanic Name")
    work_assigned = fields.Boolean(string="Work Assigned")
    repaired_cars_ids = fields.Many2many(string="Repaired Cars", comodel_name="service.appointment")
