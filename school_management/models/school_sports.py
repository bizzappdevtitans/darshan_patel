from odoo import api, fields, models


class SchoolSports(models.Model):
    _name = "school.sports"
    _description = "School Sports"
    _order = "game"
    # _order is use for sorting the records #T00341

    # attributes of player records #T00341
    name = fields.Char(string="Player name", required=True)
    game = fields.Char(required=True)
    game_type = fields.Selection([("Indoor", "Indoor"), ("Outdoor", "Outdoor")])
    player_status = fields.Boolean()
    favorites = fields.Boolean(string="Star Player")
    date_of_birth = fields.Date()
    mobile_number = fields.Char()

    # name get ovrride ORM method  #T00341
    @api.depends("name", "game")
    def name_get(self):
        """this method is for concate the name and game #T00341"""
        player_list = []
        for record in self:
            player_list.append((record.id, "[%s] : [%s]" % (record.name, record.game)))
        return player_list

    # name_search override ORM method #T00341
    @api.model
    def name_search(self, name, args=None, operator="ilike", limit=100):
        """this method is for search particular string of given records #T00341"""
        args = args or []
        if name:
            palyer_name = self.search(
                ["|", ("name", operator, name), ("game", operator, name)]
            )
            return palyer_name.name_get()
        return self.search([("name", operator, name)] + args, limit=limit).name_get()
