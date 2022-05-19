{
    'name': "Odoo Space Mission",

    'author': "My Company",
    'website': "http://www.yourcompany.com",
    'category': 'Something',
    'version': '0.1',
    'license': 'LGPL-3',

    'depends': ['base', 'project'],

    'data': [
        'security/spaceship_security.xml',
        'security/ir.model.access.csv',
        'views/spaceship_menu.xml',
        'views/spaceship_views.xml',
        'views/space_mission_views.xml',
        'views/project_project.xml',
        'wizard/create_project_views.xml',
        'reports/spaceship_missions_report.xml',
        'views/website_templates.xml',
    ],

    'demo': [
        'demo/spaceship_demo.xml'
    ],
}