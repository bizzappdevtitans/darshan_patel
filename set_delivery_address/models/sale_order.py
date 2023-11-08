from odoo import api, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    # onchange method for set auto delivery address on sale order #T00457
    @api.onchange("partner_id")
    def onchange_partner_id(self):
        """this method set address while select partner in sale order #T00457"""
        list_partner = [
            child
            for record in self.partner_id
            for child in record.child_ids
            if child.address_verified
        ]

        for record in self.partner_id:
            for child in record.child_ids:
                if len(list_partner) > 1:
                    if child == list_partner[0]:
                        values = {
                            "partner_shipping_id": child.id,
                            "partner_invoice_id": child.id,
                        }
                        self.update(values)

            for child in record.child_ids:
                if len(list_partner) == 1:
                    if child.address_verified:
                        values = {
                            "partner_shipping_id": child.id,
                            "partner_invoice_id": child.id,
                        }
                        self.update(values)
