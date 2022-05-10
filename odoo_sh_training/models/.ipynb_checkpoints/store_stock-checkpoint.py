from odoo import models, fields

class StoreStock(models.Model)

    _name = 'store.stock'
    _description = 'Store Stock'
    
    name = fields.Char('Product Name')
    quantity = fields.Integer('QTY')
    price  = fields.Float('Price')
    