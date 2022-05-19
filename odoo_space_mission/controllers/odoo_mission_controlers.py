from odoo import http


class SpaceMission(http.Controller):
    
    
    @http.route("/odoo_space/", website=True)
    def index(self):
        return "Odoo Space Mission"
    
    @http.route("/odoo_space/missions/", website=True)
    def missions(self):
        missions = http.request.env["space.mission"].search([])
        return http.request.render('odoo_space_mission.all_missions_website', {
            'missions': missions,
        })
    
    @http.route("/odoo_space/<model('space.ship'):spaceship>", website=True)
    def spaceship(self, spaceship):
        return http.request.render('odoo_space_mission.spaceship_website', {
            'spaceship': spaceship,
        })
        