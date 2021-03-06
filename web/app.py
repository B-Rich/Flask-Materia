from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from . import config

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)

from . import models
from . import views

