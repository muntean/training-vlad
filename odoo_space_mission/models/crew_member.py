from odoo import fields, models


class CrewMember(models.Model):
    _name = "crew.member"

    res_partner_id = fields.Many2one("res.partner", string="Crew Member")
    space_ship_id = fields.Many2one("space.ship")
    