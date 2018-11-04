import flask,flask_admin,flask_sqlalchemy
import sqlalchemy
from wtforms import validators

app = flask.Flask(__name__)
app.config.update(dict(FLASK_ADMIN_SWATCH='flatly',SECRET_KEY='123456790',SQLALCHEMY_DATABASE_URI='sqlite:///test.sqlite',SQLALCHEMY_ECHO=True))

db = flask_sqlalchemy.SQLAlchemy(app)

from .models import *

db.drop_all()
db.create_all()

admin = flask_admin.Admin(app, template_mode='bootstrap3')

from .views import *

