from odoo import models, api


class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.onchange('partner_id')
    def onchange_partner_id(self):
        super(SaleOrder, self).onchange_partner_id()
        list_partner = []
        for record in self.partner_id:
            for child in record.child_ids:
                if child.address_verified:
                    list_partner.append(child.name)

        for record in self.partner_id:
            for child in record.child_ids:
                if len(list_partner) > 1:
                    if child.name == list_partner[0]:
                        values = {
                            'partner_invoice_id': child.id,
                            'partner_shipping_id': child.id,
                        }
                        self.update(values)
                else:
                    if child.address_verified:
                        values = {
                            'partner_invoice_id': child.id,
                            'partner_shipping_id': child.id,
                        }
                        self.update(values)
