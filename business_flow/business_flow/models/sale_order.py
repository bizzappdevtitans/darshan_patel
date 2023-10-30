from odoo import fields, models


class SalesInherit(models.Model):
    _inherit = "sale.order"

    # fields for sale order #T00375
    invoice_description = fields.Char(string="Invoice Description")
    delivery_description = fields.Char(string="Delivery Description")
    project_description = fields.Char(string="Project Description")
    task_description = fields.Char(string="Task Description")
    purchase_description = fields.Char(string="Purchase Description")
    delivery_description = fields.Char(string="Delivery Description")
    manufacturing_description = fields.Char(string="Manufacturing Description")

    # inherit method for pass field value from sale order to invoice #T00375
    def _prepare_invoice(self):
        """this inherited method is use for pass value for sale order regular invoice #T00375"""
        invoice_values = super(SalesInherit, self)._prepare_invoice()
        """pass value to invoice #T00375"""
        invoice_values['invoice_description'] = self.invoice_description
        """pass value to delivery"""
        invoice_values['delivery_description'] = self.delivery_description
        return invoice_values


class SaleAdvancePaymentInv(models.TransientModel):
    _inherit = 'sale.advance.payment.inv'

    # inherit method for pass field value from sale order to invoice #T00375
    def _prepare_invoice_values(self, order, name, amount, so_line):
        """this inherited method is use for pass value for sale order downpayment invoice #T00375"""
        invoice_values = super(SaleAdvancePaymentInv, self)._prepare_invoice_values(
            order, name, amount, so_line
        )
        """pass value to invoice #T00375"""
        invoice_values.update({"invoice_description": order.invoice_description})
        """pass value to delivery"""
        invoice_values.update({"delivery_description": order.delivery_description})
        return invoice_values


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    # inherit method for pass field value from sale order to project #T00384
    def _timesheet_create_project_prepare_values(self):
        """this method pass field value from sale order to project #T00384"""
        project_values = super(
            SaleOrderLine, self
        )._timesheet_create_project_prepare_values()
        project_values["project_description"] = self.order_id.project_description
        return project_values

    # inherit method for pass field value from sale order to task #T00384
    def _timesheet_create_task_prepare_values(self, project):
        """this method pass field value from sale order to task #T00384"""
        task_values = super(SaleOrderLine, self)._timesheet_create_task_prepare_values(
            project
        )
        task_values["task_description"] = self.order_id.task_description
        return task_values


class StockRule(models.Model):
    _inherit = 'stock.rule'

    # this inherit method is use for pass value into purchase order #T00388
    def _prepare_purchase_order(self, company_id, origins, values):
        """ this method pass value from stock to purchase order #T00388 """
        val = super(StockRule, self)._prepare_purchase_order(company_id, origins, values)
        val['purchase_description'] = values[0].get("purchase_description").purchase_description
        return val

    # this inherit method is pass field value from stock to mrp #T00405
    def _prepare_mo_vals(self, product_id, product_qty, product_uom, location_id, name, origin, company_id, values, bom):
        """this method is use for pass value from stock to mrp(manufacturing order) #T00405"""
        res = super()._prepare_mo_vals(product_id, product_qty, product_uom, location_id, name, origin, company_id, values, bom)
        res['manufacturing_description'] = values.get('manufacturing_description')
        return res
