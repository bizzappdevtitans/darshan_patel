from datetime import date

from dateutil import relativedelta

from odoo.tests.common import TransactionCase


class TestSchoolLibrary(TransactionCase):
    # setUp method for create new record of books #T00467
    def setUp(self):
        """this method is create  new record #T00467"""
        super(TestSchoolLibrary, self).setUp()
        self.record_01 = self.env["school.library"].create(
            {
                "code": 47058,
                "name": "History",
                "book_author": "K M SHARMA",
                "book_issue_date": date.today(),
            }
        )

    # test method for check the output of methods #T00467
    def test_01(self):
        """this method is check the output of the function #T00467"""
        self.assertEqual(
            self.record_01.book_return_date,
            self.record_01.book_issue_date + relativedelta.relativedelta(months=2),
        )
