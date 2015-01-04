from web.app import db
from web.controllers import create_post

db.create_all()
create_post('Test Post', 'Test body', 'Test Cat')

# Expected results: