# -*- coding: utf-8 -*-
from odoo import models, fields, api


class MprProduction(models.Model):
    _inherit = 'mrp.production'

    @api.model
    def _get_sale_order(self):
        for record in self:
            sale_obj = self.env['sale.order']
            if record.origin:
                sale_id = sale_obj.search([('name', '=', record.origin)])
                if sale_id:
                    for line in sale_id.order_line.filtered(
                            lambda l: l.product_id.id == record.product_id.id):
                        record.sale_order_line_id = line.id
                    record.sale_id = sale_id.id

    sale_id = fields.Many2one(
        comodel_name='sale.order',
        string='Sale related',
        readonly=True,
        copy=False,
        compute="_get_sale_order"
    )
    sale_order_line_id = fields.Many2one(
        comodel_name='sale.order.line',
        string='Sale order line related',
        readonly=True,
        copy=False,
        compute="_get_sale_order"
    )


