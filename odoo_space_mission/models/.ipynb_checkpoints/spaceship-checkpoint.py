from odoo import models, fields


class SpaceShip(models.Model):
    
    _name = "space.ship"
    _description = "An aircraft that can go to the moon"
    
    model = fields.Char("Spaceship Model")
    description = fields.Text("Description")
    crew_type = fields.Selection(string="Crew Type", selection=[('small', 'Small Crew'),
                                                         ('medium', 'Medium Crew'),
                                                         ('large', 'Large Crew')])
    crew_size = fields.Integer("Nr of people in crew")
    active = fields.Boolean("Active", default=True)