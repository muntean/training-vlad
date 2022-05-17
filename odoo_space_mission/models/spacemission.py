from odoo import models, fields


class SpaceMission(models.Model):
    _name = "space.mission"
    _description = "A space mission."
    
    name = fields.Char("Name")
    start_date = fields.Date("Start Date")
    end_date = fields.Date("End Date")
    
    spaceship_id = fields.Many2one("space.ship", "Spaceship")
    
    crew_ids = fields.Many2many("res.partner", string="Crew")
    
    amount_of_fuel_needed = fields.Float(string="Fuel needed(liters)")
    
    number_of_engines = fields.Integer("Number of engines")
    