from odoo.tests.common import TransactionCase
from odoo.tests import common
from odoo.exceptions import ValidationError


class TestWizardCancelAppointment(TransactionCase):
    # setUP method for create record for test cases #T00470
    def setUp(self):
        super(TestWizardCancelAppointment, self).setUp()
        # create record for appointment #T00470
        self.appointment_01 = self.env["service.appointment"].create(
            {
                "name": "Mr. Janak",
                "contact_number": 1234567891,
                "customer_mail": "janak@bizzappdev.com",
                "car_model": "mercedes",
                "car_number": "GJ08GY4785",
                "appointment_date": "2024-12-12",
                "car_sevices_ids": self.env.ref("automotive_service_management.automotive_accessories_1"),
            }
        )

        # create record for wizard #T00470
        self.cancel_appointment_01 = self.env['cancel.appointment'].create(
            {
                "appointment_ids": self.appointment_01.id
            }
            )
        self.appointment_01.button_in_service()

    # test_action_cancel_service_appointment for call wizard function #T00470
    def test_action_cancel_service_appointment(self):
        """this method is call wizard function with validation or without
        validation #T00470"""
        self.cancel_appointment_01.action_cancel_service_appointment()

        with self.assertRaises(ValidationError):
            self.cancel_appointment_01.action_cancel_service_appointment()
