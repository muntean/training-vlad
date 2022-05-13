from odoo import models, fields, api
from odoo.exceptions import UserError


class SpaceShip(models.Model):
    _name = "space.ship"
    _description = "An aircraft that can go to the moon"
    _rec_name = "model"

    model = fields.Char("Spaceship Model")
    description = fields.Text("Description")
    crew_type = fields.Selection(string="Crew Type", selection=[('small', 'Small Crew'),
                                                                ('medium', 'Medium Crew'),
                                                                ('large', 'Large Crew')])
    crew_size = fields.Integer("Crew size")
    active = fields.Boolean("Active", default=True)
    
    width = fields.Float("Width")
    length = fields.Float("Length")
    
    @api.constrains('width', 'length')
    def _check_width_less_than_length(self):
        for item in self:
            if item.width > item.length:
                raise UserError('The aircraft width cannot be bigger than the length!')
