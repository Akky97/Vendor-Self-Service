# -*- coding: utf-8 -*-

from odoo import models, fields, api


class VendorForecast(models.Model):
    _name = 'vendor.forecast'
    _description = 'Vendor Forecast'

    product_id = fields.Many2one('product.product', string='Product')
    expected_quantity = fields.Integer('Expected Quantity')
    forecast_date = fields.Date('Forecast Date')


class VendorAdjustmentRequest(models.Model):
    _name = 'vendor.adjustment.request'
    _description = 'Vendor Adjustment Request'

    order_id = fields.Many2one('sale.order', string='Order')
    adjustment_detail = fields.Text('Adjustment Detail')
    comment = fields.Text('Comment')

    @api.model
    def create(self, vals_list):
        rec = super().create(vals_list)
        email_template = self.env.ref('vendor_self_service_portal.email_template_notification')
        outgoing_server_name = self.env['ir.mail_server'].sudo().search([], limit=1)
        if email_template and outgoing_server_name:
            email_template.email_from = f"{outgoing_server_name.name}"
            email_template.email_to = rec.order_id.partner_id.email
            email_template.body_html = f"""
                <div style="font-family: 'Lucica Grande', Ubuntu, Arial, Verdana, sans-serif; font-size: 12px; color: rgb(34, 34, 34); background-color: #FFF; ">
                    <p>Hi {rec.order_id.partner_id.name},</p>
                    <p>This is to notify that we have create a new request. please check it.</p>
                    <p>Thanks,</p>
                    <p>Fatmug Designs Team</p>                                    
                </div>
            """
            email_template.send_mail(rec.id, force_send=True)
        return rec

