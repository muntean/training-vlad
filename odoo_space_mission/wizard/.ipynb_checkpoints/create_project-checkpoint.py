from odoo import models, fields


class CreateProjectWizard(models.TransientModel):
    _name = "create.project.wizard"
    
    def _get_space_mission(self):
        return self.env["space.mission"].browse(self._context.get("active_id"))
    
    name = fields.Char("Name of Project")
    start_date = fields.Date("Start date", default=fields.Date.today)
    end_date = fields.Date("End date")
    space_mission_id = fields.Many2one("space.mission", string="Space mission", default=_get_space_mission)   
    
    def create_project(self):
        for item in self:
            self.env["project.project"].create({
                "name": item.name,
                "date_start": item.start_date,
                "date": item.end_date,
                "space_mission_id": item.space_mission_id.id,
                "is_space_project": True
            })