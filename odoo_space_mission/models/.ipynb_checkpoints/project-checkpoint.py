from odoo import fields, models


class Project(models.Model):
    _inherit = "project.project"

    space_mission_id = fields.Many2one("space.mission")
    
    is_space_project = fields.Boolean("Is Space Project")