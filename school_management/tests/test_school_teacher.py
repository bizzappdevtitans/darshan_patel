from odoo.exceptions import ValidationError
from odoo.tests.common import TransactionCase


class TestSchoolTeacher(TransactionCase):
    # setUp method for create new record of student #T00467
    def setUp(self):
        """this method is create  new record #T00467"""
        super(TestSchoolTeacher, self).setUp()
        self.teacher_01 = self.env["school.teacher"].create(
            {"name": "Prof. Rahul", "subject": "maths", "teacher_phone": 1234567890}
        )
        with self.assertRaises(ValidationError):
            vals = {
                "name": "Prof. AMBIKA",
                "subject": "ADA",
                "teacher_phone": 123456789,
            }
            self.teacher_02 = self.env["school.teacher"].create(vals)

    def test_01(self):
        self.assertEqual(self.teacher_01.name, "Prof. Rahul")
