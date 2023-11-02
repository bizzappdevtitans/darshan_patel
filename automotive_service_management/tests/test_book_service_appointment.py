from odoo.tests.common import TransactionCase
from odoo.tests import common
from odoo.exceptions import ValidationError


class TestBookServiceAppointment(TransactionCase):
    # setUP method for create record for test cases #T00470
    def setUp(self):
        super(TestBookServiceAppointment, self).setUp()
        # create record for wizard #T00470
        self.appointment_01 = self.env["book.appointment"].create(
            {
                "name": "Mr. Joe",
                "mobile_number": 1234567891,
                "customer_mail": "joe@bizzappdev.com",
                "car_model": "Range Rover",
                "car_number": "GJ09TY6754",
                "appointment_date": "2024-12-12",
                "select_service": self.env.ref("automotive_service_management.automotive_accessories_1"),
            }
        )

    # method for call wizard book appointment method #T00470
    def test_book_service_appointment(self):
        """this method is use to call wizard book appointment method #T00470"""
        self.appointment_01.action_book_appointment()
