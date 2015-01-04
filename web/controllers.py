from app import db
from models import Post

# Simple CRUD for our posts

def get_all_posts():
  return Post.query.all()

def create_post(title, body, category,):
  post = Post(title, body, category)
  db.session.add(post)
  db.session.commit()

def update_post(id, title, body, category):
  post = Post.query.filter_by(id=id).first()
  post.title = title
  post.body = body
  post.category = category
  db.session.commit()

def delete_post(id):
  post = Post.query.filter_by(id=id).first()
  db.session.delete(post)
  db.session.commit()
