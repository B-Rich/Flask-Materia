from app import app
from flask import render_template, request
from controllers import get_posts, get_all_posts, get_category_list, get_posts_with_category

@app.route("/blog")
def blog():
  return render_template('blog.html', posts=get_posts(9), categories=get_category_list())

@app.route("/blog/category/<category>")
def category(category):
  # Searches for all posts in a certain category
  return render_template('blog.html', posts=get_posts_with_category(category), categories=get_category_list())

@app.route("/blog/editor")
def editor():
  return render_template('editor.html')

@app.route("/test")
def test():
  result = get_category_list()
  return "!"