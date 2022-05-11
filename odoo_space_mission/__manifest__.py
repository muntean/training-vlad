{
    'name': "Odoo Space Mission",

    'author': "My Company",
    'website': "http://www.yourcompany.com",
    'category': 'Something',
    'version': '0.1',
    'license': 'LGPL-3',

    'depends': ['base', ],

    'data': [
        'security/spaceship_security.xml',
        'security/ir.model.access.csv',
    ],

    'demo': [
        'demo/spaceship_demo.xml'
    ],
}