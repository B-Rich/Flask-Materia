from app import db
from models import Post
from flask.ext.sqlalchemy import SQLAlchemy

# Simple CRUD for our posts

def get_all_posts():
  return Post.query.order_by(Post.pub_date.desc()).all()

def get_posts(limit):
  return Post.query.order_by(Post.pub_date.desc()).limit(limit)

def get_posts_with_category(category):
  return Post.query.filter_by(category=category).order_by(Post.pub_date.desc()).all()

def get_category_list():
  """ Get a unique list of all categories and their counts """
  # Returns a KeyedTuple
  posts =  db.session.query(Post.category, db.func.count(Post.id)).group_by(Post.category).all()

  return posts

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
