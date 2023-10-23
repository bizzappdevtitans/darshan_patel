# -*- coding: utf-8 -*-

from odoo import models, fields, api
from dateutil import relativedelta
from datetime import date
from odoo.exceptions import ValidationError


class ServiceAppointment(models.Model):
    _name = 'service.appointment'
    _description = 'service.appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Customer Name")
    contact_number = fields.Char(string="Mobile Number")
    appointment_number = fields.Char(string="Appointment Number", readonly=True)
    car_model = fields.Char(string="Car Model Name")
    car_number = fields.Char(string="Car Number")
    appointment_date = fields.Date(string="Appointment Date")
    delivery_date = fields.Date(string="Delivery Date", compute="_compute_delivery_date")
    car_sevices_ids = fields.Many2many(comodel_name="automotive.accessories", string="Services")
    assigned_mechanic = fields.Many2one(comodel_name="automotive.mechanic", string="Assigned To")
    total_cost = fields.Integer(string="Total Cost", compute="_compute_total_cost", readonly="True")

    state = fields.Selection(
        [
            ("appointed", "Appointed"),
            ("in_service", "In Service"),
            ("serviced", "Serviced"),
        ],
        string="Status",
        required=True,
        default="appointed",
        tracking=True
    )

    def button_appointed(self):
        self.write({"state": "appointed"})

    def button_in_service(self):
        self.write({"state": "in_service"})
        for mechanic in self.assigned_mechanic:
            if mechanic.work_assigned:
                raise ValidationError(f"{mechanic.name} is busy please select another one or wait till finish work.")
            else:
                mechanic.write({'work_assigned': 'True'})

    def button_serviced(self):
        self.write({"state": "serviced"})
        mechanics = self.env['automotive.mechanic'].search([])
        for record in mechanics:
            if record.name == self.assigned_mechanic.name:
                record.repaired_cars_ids = [(4, self.id)]
                record.write({'work_assigned': 0})
        mail_template = self.env.ref("automotive_service_management.serviced_car_mail")
        mail_template.send_mail(self.id, force_send=True)

    @api.model
    def create(self, vals):
        vals['appointment_number'] = self.env['ir.sequence'].next_by_code("service.appointment")
        return super(ServiceAppointment, self).create(vals)

    @api.depends('name', 'appointment_number')
    def name_get(self):
        record_list = []
        for record in self:
            record_list.append((record.id, "[%s] : [%s]" % (record.appointment_number,
                                                            record.name)))
        return record_list

    @api.model
    def name_search(self, name, args=None, operator="ilike", limit=100):
        args = args or []
        if name:
            recs = self.search(['|', ("appointment_number", operator, name),
                               ("name", operator, name)])
            return recs.name_get()
        return self.search([("name", operator, name)]+args, limit=limit).name_get()

    @api.depends('appointment_date')
    def _compute_delivery_date(self):
        service_duration = self.env['ir.config_parameter'].get_param(
            "automotive_service_management.service_duration")
        for record in self:
            record.delivery_date = record.appointment_date + relativedelta.relativedelta(days=int(service_duration))

    def action_send_mail(self):
        records = self.env['service.appointment'].search([])
        for record in records:
            if record.appointment_date == date.today():
                mail_template = self.env.ref("automotive_service_management.service_appointment_mail")
                mail_template.send_mail(record.id, force_send=True)

    @api.onchange('car_sevices_ids')
    def _compute_total_cost(self):
        for record in self:
            sum_of_lines = sum(record.car_sevices_ids.mapped('service_charge'))
            record.total_cost = sum_of_lines
