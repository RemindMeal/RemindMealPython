from flask import Flask
from flask.ext.admin import Admin
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
admin = Admin(app, name="RemindMeal", template_mode="bootstrap3")

from views import MealView

admin.add_view(MealView(db.session))
