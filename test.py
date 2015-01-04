from web.app import app, db
from web.controllers import get_all_posts, create_post, update_post, delete_post
from web.models import Post

# Simple barebone tests. TODO: Use a well-known plugin

failing = []

# Delete all posts, clean slate

Post.query.delete()
db.session.commit()

# Test 1: CRUD Test

create_post('Test Post', 'Test body', 'Test Cat')
create_post('Test Post 2', 'Test body 2', 'Test Cat 2')
update_post(1, 'Updated Post', 'Updated Body', 'Updated Catty')
delete_post(2)

post = Post.query.filter_by(id=1).first()

# Expected results: '1 | Today's date i.e. 2015-01-04 09:12:53.928927 | Updated Post | Updated Body | Updated Catty'

if (len(Post.query.all()) == 1 and
  post.title == 'Updated Post' and
  post.body == 'Updated Body' and
  post.category == 'Updated Catty'):
  print "PASS 1"
else:
  failing.append('1: CRUD TEST')
  print "FAIL 1"

if len(failing) == 0:
  print "All tests passed!"
else:
  print "Failed {0} tests: {1}".format(len(failing), ', '.join(failing))

