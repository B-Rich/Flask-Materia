from web.app import app, db
from web.controllers import get_posts, create_post, update_post, delete_post
from web.models import Post

# Simple barebone backend tests
# TODO: Use a well-known plugin

failing_tests = []

# Delete all posts
def clean_slate():
  Post.query.delete()
  db.session.commit()

# Test 1: CRUD Test
clean_slate()
create_post('Test Post', 'Test Flavor', 'http://placehold.it/300x200', 'Test body', 'Test Cat')
create_post('Test Post 2', 'Test Flavor2', 'http://placehold.it/300x200', 'Test body 2', 'Test Cat')
update_post(1, 'Updated Post', 'Updated Flavor', 'http://placehold.it/300x200', 'Updated Body', 'Updated Catty')
delete_post(2)

post = Post.query.filter_by(id=1).first()

if (len(Post.query.all()) == 1 and
  post.title == 'Updated Post' and
  post.flavor_text == 'Updated Flavor' and
  post.body == 'Updated Body' and
  post.category == 'Updated Catty'):
  print "PASS 1"
else:
  failing_tests.append('1: CRUD TEST')
  print "FAIL 1"

# Place more tests here

if len(failing_tests) == 0:
  print "All tests passed!"
else:
  print "Failed {0} tests: {1}".format(len(failing_tests), ', '.join(failing_tests))

# Populate initial cards

create_post('Test Post 2', 'Test Flavor', 'http://placehold.it/300x200', 'Test body', 'Foo')
create_post('Test Post 3', 'Test Flavor', 'http://placehold.it/300x200', 'Test body', 'Foo')
create_post('Test Post 4', 'Test Flavor', 'http://placehold.it/300x200', 'Test body', 'Spam')