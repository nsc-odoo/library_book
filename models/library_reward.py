from odoo import models, fields, api

class Reward(models.Model):
    _name='library.reward'
    _descrption='Book Reward'
    
    title = fields.Char(
        string='title', 
        required=True
    )
    amount = fields.Integer(
        string='amount'
    )
    
    book_id = fields.Many2one(
        'library.book',
        string='book',
        ondelete='restrict',
    )
