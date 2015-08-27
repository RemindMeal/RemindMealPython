from flask import Flask
from flask.ext.admin import Admin, AdminIndexView
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.babelex import Babel
from flask.ext.security import Security, SQLAlchemyUserDatastore

app = Flask(__name__)
app.config.from_object('config')
app.jinja_env.autoescape = False

db = SQLAlchemy(app)

admin = Admin(app, name="RemindMeal", template_mode="bootstrap3",
              index_view=AdminIndexView(name='Home', url='/'))

from views import *

admin.add_view(CategoryView(db.session))
admin.add_view(FriendView(db.session))
admin.add_view(MealView(db.session))
admin.add_view(RecipeView(db.session))
admin.add_view(LoginView(name="Connexion"))
admin.add_view(RegisterView(name="S'enregistrer"))
admin.add_view(LogoutView(name="Deconnexion"))

babel = Babel(app, default_locale='fr')

from app.entity.user import Role, User
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)
