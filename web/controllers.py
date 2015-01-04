from app import db
from models import Post

# Simple CRUD for our posts

def get_all_posts():
  return Post.query.all()

def create_post(title, flavor_text, small_img_url, body, category):
  post = Post(title, flavor_text, small_img_url, body, category)
  db.session.add(post)
  db.session.commit()

def update_post(id, title, flavor_text, small_img_url, body, category):
  post = Post.query.filter_by(id=id).first()
  post.title = title
  post.flavor_text = flavor_text
  post.small_img_url = small_img_url
  post.body = body
  post.category = category
  db.session.commit()

def delete_post(id):
  post = Post.query.filter_by(id=id).first()
  db.session.delete(post)
  db.session.commit()
