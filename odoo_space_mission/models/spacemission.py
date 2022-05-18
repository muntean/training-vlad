from odoo import models, fields


class SpaceMission(models.Model):
    _name = "space.mission"
    _description = "A space mission."
    
    name = fields.Char("Name")
    start_date = fields.Date("Start Date")
    end_date = fields.Date("End Date")
    
    spaceship_id = fields.Many2one("space.ship", "Spaceship")
    
    crew_ids = fields.Many2many("res.partner", string="Crew")

    crew_contacts_ids = fields.Many2many(related="crew_ids", string="Crew Contacts")
    
    amount_of_fuel_needed = fields.Float(string="Fuel needed(liters)")
    
    number_of_engines = fields.Integer("Number of engines")
    
    space_mission_location = fields.Many2one("res.partner", string="Location")

    project_ids = fields.One2many("project.project", "space_mission_id", string="Projects")
    