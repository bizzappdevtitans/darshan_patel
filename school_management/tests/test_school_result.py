from datetime import date

from odoo.exceptions import ValidationError
from odoo.tests.common import TransactionCase


class TestSchoolResult(TransactionCase):
    # setUp method for create new record of books #T00467
    def setUp(self):
        """this method is create  new record #T00467"""
        super(TestSchoolResult, self).setUp()
        self.record_01 = self.env["school.result"].create(
            {
                "name": "Dhyan",
                "enroll_number": "21020345789",
                "standard": 10,
                "chemistry": 85,
                "maths": 85,
                "physics": 85,
                "date_start": date.today(),
            }
        )
        self.record_01.name_get()
        self.record_01.name_search(
            self.record_01.name, args=None, operator="ilike", limit=100
        )
        self.record_01.copy()

        self.record_02 = self.env["school.result"].create(
            {
                "name": "Anurag",
                "enroll_number": "21020345789",
                "standard": 10,
                "chemistry": 86,
                "maths": 86,
                "physics": 86,
                "date_start": date.today(),
            }
        )
        self.recheck_result_01 = self.env["recheck.result"].create(
            {"enrollment_number_id": self.record_02.id}
        )

        self.record_03 = self.env["school.result"].create(
            {
                "name": "Krish",
                "enroll_number": "21020345789",
                "standard": 10,
                "chemistry": 86,
                "maths": 86,
                "physics": 86,
                "date_start": "2023-01-01",
            }
        )
        self.recheck_result_02 = self.env["recheck.result"].create(
            {"enrollment_number_id": self.record_03.id}
        )

    # test method for check the output of methods #T00467
    def test_01(self):
        """this method is check the output of the function #T00467"""
        self.assertEqual(self.record_01.marks, 85)

    def test_action_recheck(self):
        self.recheck_result_01.action_recheck()

        with self.assertRaises(ValidationError):
            self.recheck_result_02.action_recheck()
