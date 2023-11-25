# -*- coding: utf-8 -*-

from odoo import models, fields, api
#
#
# class PosOrder(models.Model):
#     _inherit = "pos.order"
#
#     sub_total = fields.Float(string='Sub Total')
#
#     def write(self, values):
#         res = super().write(values)
#         if not values.get('sub_total'):
#             sub_total = 0.0
#             for line in self.lines:
#                 if self.session_id.config_id.discount_product_id.id != line.product_id.id:
#                     sub_total += line.price_unit * line.qty
#             self.sub_total = sub_total
#         return res
#
class PosOrder(models.Model):
    _name = "pos.order"
    _inherit = ['pos.order', 'mail.thread', 'mail.activity.mixin']

    def get_lot_available(self, msg, product):
        rec = self.env['stock.production.lot'].sudo().search([('name', '=', msg), ('product_id', '=', product)])
        if rec:
            return True
        else:
            return False

    @api.returns('mail.message', lambda value: value.id)
    def message_post(self, **kwargs):
        return super(PosOrder, self.with_context(mail_post_autofollow=True)).message_post(**kwargs)


class PosOrderLine(models.Model):
    _inherit = "pos.order.line"

    def create(self, values):
        message = ""
        for vals in values:
            if vals.get('order_id'):
                for rec in vals.get('pack_lot_ids'):
                    vv = self.env['stock.production.lot'].sudo().search([('name', '=', rec[2]['lot_name']), ('product_id', '=', vals.get('product_id'))])
                    if not vv:
                        message = f"{rec[2]['lot_name']} is unavailable in stock"
                if message:
                    order = self.env['pos.order'].sudo().browse(int(vals.get('order_id')))
                    order.message_post(body=message)
        return super(PosOrderLine, self).create(values)

