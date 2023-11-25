# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class LoyaltySaleReport(models.Model):
    _name = "loyalty.sale.report"

    loyalty_program_id = fields.Many2one('loyalty.program', string="Program Name")
    product_id = fields.Many2one('product.product',string="Product")
    order_id = fields.Many2one('sale.order', string='Order')
    partner_id = fields.Many2one('res.partner', string='User')
    date = fields.Date(string='Date')
    qty = fields.Float(string='Qty')
    mobile = fields.Char(string='Mobile')
    used_coupon_code = fields.Char(string='Used Coupon Code')

