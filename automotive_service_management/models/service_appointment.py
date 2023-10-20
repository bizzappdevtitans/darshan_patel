# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ServiceAppointment(models.Model):
    _name = 'service.appointment'
    _description = 'service.appointment'

    name = fields.Char(string="Customer Name")
    appointment_number = fields.Char(string="Appointment Number", readonly=True)
    car_model = fields.Char(string="Car Model Name")
    car_number = fields.Char(string="Car Number")
    appointment_date = fields.Date(string="Appointment Date")
    car_sevices_ids = fields.Many2many(comodel_name="automotive.accessories", string="Services")
    assigned_mechanic = fields.Many2one(comodel_name="automotive.mechanic", string="Assigned To")

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
