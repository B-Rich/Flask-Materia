from app import db
from models import Post

def get_all_posts():
  posts = Post.query.all()
  result = []

  for i in posts:
    result.append(i)

  return result

def create(title, body, category,):
  post = Post(title, body, category)

  db.session.add(post)
  db.session.commit()
