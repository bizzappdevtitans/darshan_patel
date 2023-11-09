from odoo.tests.common import TransactionCase


class TestSchoolSports(TransactionCase):
    # setUp method for create new record of student #T00467
    def setUp(self):
        """this method is create  new record #T00467"""
        super(TestSchoolSports, self).setUp()
        self.player_01 = self.env["school.sports"].create(
            {"name": "brij", "game": "Cricket", "mobile_number": 1234567890}
        )
        self.player_01.name_get()
        self.player_01.name_search(self, args=None, operator="ilike", limit=100)

    # test method for check the output of methods #T00467
    def test_01(self):
        """this method is check the output of the function #T00467"""
        self.assertEqual(self.player_01.name, "brij")
