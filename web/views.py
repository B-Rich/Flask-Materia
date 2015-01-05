from app import app
from flask import render_template
from controllers import get_posts

@app.route("/")
def index():
  return render_template('index.html', posts=get_posts(9))

@app.route("/editor")
def editor():
  return render_template('editor.html')

@app.route("/test")
def test():
  """ Temporary debugging function """
  result = ""
  for i in get_all_posts():
    result = result + "{0} | {1} | {2} | {3} | {4} <br>".format(i.id, i.pub_date, i.title, i.body, i.category)
  return result