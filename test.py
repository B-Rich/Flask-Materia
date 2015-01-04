from web.app import db
from web.controllers import create_post, update_post, delete_post
from web.models import Post

# Delete all posts, clean slate

Post.query.delete()
db.session.commit()

create_post('Test Post', 'Test body', 'Test Cat')
create_post('Test Post 2', 'Test body 2', 'Test Cat 2')
update_post(1, 'Updated Post', 'Updated Body', 'Updated Catty')
delete_post(2)

# Expected results: '1 | Today's date i.e. 2015-01-04 09:12:53.928927 | Updated Post | Updated Body | Updated Catty'