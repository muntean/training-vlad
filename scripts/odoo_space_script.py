from xmlrpc import client

url = 'https://training-training-vlad-vlad-odoo-space-ship-4977241.dev.odoo.com'
db = 'training-training-vlad-vlad-odoo-space-ship-4977241'
username = 'admin'
password = 'admin'

common = client.ServerProxy("{}/xmlrpc/2/common".format(url))
print(common.version())

uid = common.authenticate(db ,username, password, {})
print(uid)

models = client.ServerProxy("{}/xmlrpc/2/object".format(url))
model_access = models.execute_kw(db, uid, password,
                                'space.ship', 'check_access_rights',
                                ['write'], {'raise_exception': False})
print(model_access)

spaceships = models.execute_kw(db, uid, password,
                              'space.ship', 'search_read',
                              [[]])
print(spaceships)

spaceship = models.execute_kw(db, uid, password,
                             'space.ship', 'search',
                             [[['model', '=', 'LFX940']]])
print(spaceship)

new_spaceship = models.execute_kw(db, uid, password,
                                 'space.ship', 'create',
                                 [
                                     {
                                         'model': 'LFZ:200',
                                         'crew_type': 'small',
                                         'crew_size': 5,
                                         'width': 50,
                                         'length': 250,                                         
                                     }
                                 ])
print(new_spaceship)

read_new_spaceship = models.execute_kw(db,uid,password,
                                      'space.ship', 'search_read',
                                      [[['model', '=', 'LFZ:200']]])
print(read_new_spaceship)