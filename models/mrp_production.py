# -*- coding: utf-8 -*-
from odoo import models, fields, api


class MprProduction(models.Model):
    _inherit = 'mrp.production'

    @api.model
    def _get_sale_order(self):
        for production in self:
            sale_obj = self.env['sale.order']
            if production.origin:
                sale_id = sale_obj.search([('name', '=', production.origin)])
                production.sale_id = sale_id.id if sale_id else False

    sale_id = fields.Many2one(
        comodel_name='sale.order',
        string='Sale related',
        readonly=True,
        copy=False,
        compute="_get_sale_order"
    )


