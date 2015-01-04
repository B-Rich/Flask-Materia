from app import db
from datetime import datetime

class Post(db.Model):
  """ Simple Post class that basically will be created using a title, body and a single category """

  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(80))
  body = db.Column(db.Text)
  pub_date = db.Column(db.DateTime)
  category = db.Column(db.String(80))

  def __init__(self, title, body, category, pub_date=None):
    self.title = title
    self.body = body

    if pub_date is None:
      pub_date = datetime.utcnow()

    self.pub_date = pub_date
    self.category = category

  def __repr__(self):
    return '<Post %r>' % self.title
