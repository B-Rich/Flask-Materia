from app import app
from controllers import get_all_posts

@app.route("/")
def hello():
  result = ""
  for i in get_all_posts():
    result = result + i.title + "<br>"
  return result