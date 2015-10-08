from flask import Flask
from flask.ext.admin import Admin, AdminIndexView, helpers as admin_helpers
from flask.ext.debugtoolbar import DebugToolbarExtension
from flask.ext.mail import Mail
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.babelex import Babel
from flask.ext.security import Security, SQLAlchemyUserDatastore

app = Flask(__name__)
app.config.from_object('config')
app.jinja_env.autoescape = False

db = SQLAlchemy(app)

admin = Admin(app, name="RemindMeal", template_mode="bootstrap3",
              index_view=AdminIndexView(name='Home', url='/'))

toolbar = DebugToolbarExtension(app)

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
mail = Mail(app)

@security.context_processor
def security_context_processor():
    return dict(admin_base_template=admin.base_template, admin_view=admin.index_view, h=admin_helpers)
