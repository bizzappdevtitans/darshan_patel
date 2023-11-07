from odoo.exceptions import ValidationError
from odoo.tests.common import TransactionCase


class TestSchoolStudent(TransactionCase):
    # setUp method for create new record of student #T00467
    def setUp(self):
        """this method is create  new record and apply below used method on record #T00467"""
        super(TestSchoolStudent, self).setUp()
        self.student_01 = self.env["student.name"].create(
            {"name": "Rahul", "marks": 70, "date_of_birth": "2019-01-01"}
        )
        self.student_01._compute_count_records()
        self.student_01.button_study()
        self.student_01._compute_student_age()
        self.student_01.button_admitted()
        self.student_01.button_drop_out()
        self.student_01.button_passed()
        self.student_01.new_record_list()

        with self.assertRaises(ValidationError):
            self.student_01.unlink()

        self.student_02 = self.env["student.name"].create(
            {"name": "Mohan", "marks": 75, "date_of_birth": "2014-01-01"}
        )
        self.student_02.button_admitted()
        self.student_02.unlink()

        self.select_player_01 = self.env["select.player"].create(
            {"name": self.student_01.id, "game": "Cricket"}
        )

    # test method for check the output of methods #T00467
    def test_01(self):
        """this method is check the output of the function #T00467"""
        self.assertEqual(self.student_01.student_age, 4)

    def test_action_select_player(self):
        self.select_player_01.action_select_player()
