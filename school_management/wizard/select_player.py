from odoo import fields, models


class SelectPlayer(models.TransientModel):
    _name = "select.player"
    _description = "Select Player"

    # field for enroll number of student #T00365
    name = fields.Many2one(comodel_name="student.name", string="Player Number")
    game = fields.Char(string="Player Game")

    # function for get field value #T00365
    def action_select_player(self):
        """this function is create value as per wizard #T00365"""
        vals = {
            "name": self.name.name,
            "game": self.game,
        }
        self.env["school.sports"].create(vals)
