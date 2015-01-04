from web.app import db
from web.controllers import create

db.create_all()

create('Test Post', 'Test body', 'Test Cat')