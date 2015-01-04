from app import app
from controllers import get_all_posts

@app.route("/")
def hello():
  """ Temporary debugging function """
  result = ""
  for i in get_all_posts():
    result = result + "{0} | {1} | {2} | {3} | {4} <br>".format(i.id, i.pub_date, i.title, i.body, i.category)
  return result