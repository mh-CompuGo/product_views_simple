from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit= "product.template"

    length = fields.Integer()
    height = fields.Integer()
    width = fields.Integer()
    owner = fields.Many2one('res.partner')