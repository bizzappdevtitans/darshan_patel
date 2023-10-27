from odoo.tests.common import TransactionCase
from odoo.tests import common


class TestServiceAppointment(TransactionCase):
    def setUp(self):
        super(TestServiceAppointment, self).setUp()
        self.appointment_01 = self.env["service.appointment"].create(
            {
                "name": "Rohan",
                "car_model": "VOLVO",
                "car_number": "GJ02DR5677",
                "car_sevices_ids": self.env["automotive.accessories"].create(
                    {
                        "name": "accessories",
                        "service_charge": 100,
                        "accessories_name": "accessories",
                    }
                ),
            }
        )
        self.appointment_02 = self.env["service.appointment"].create(
            {"name": "Mohan", "car_model": "Audi", "car_number": "GJ02DR5677"}
        )
        self.appointment_01.button_appointed()
        self.appointment_01.button_in_service()
        self.appointment_01.action_send_mail()
        self.appointment_01._compute_delivery_date()
        self.appointment_01._compute_total_cost()
        self.appointment_01.name_search(self, args=None, operator="ilike", limit=100)
        self.appointment_01.name_search(self, args=None, operator="ilike", limit=100)

    def test_01(self):
        self.assertEqual(self.appointment_01.total_cost, 100)
        self.assertEqual(self.appointment_01.state, "in_service")

        self.appointment_01.button_serviced()
        self.assertEqual(self.appointment_01.state, "serviced")
        self.assertEqual(self.appointment_01.assigned_mechanic.work_assigned, False)

        self.appointment_02.button_appointed()
        self.assertEqual(self.appointment_02.state, "appointed")
