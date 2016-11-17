# coding: utf8

from flask import Flask, render_template, flash, redirect, request, url_for
from flask_admin import AdminIndexView, Admin, helpers as admin_helpers
from flask_babelex import Babel
from flask_debugtoolbar import DebugToolbarExtension
from flask_login import current_user
from flask_security import Security, SQLAlchemyUserDatastore
from flask_sqlalchemy import SQLAlchemy
from raven.contrib.flask import Sentry

app = Flask(__name__)
app.config.from_object('config')
app.jinja_env.autoescape = False
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

DebugToolbarExtension(app)
Babel(app, default_locale='fr')
# Sentry(app)

from app.models import db, User, Role
db.init_app(app)

from app.firewall import Role, User, MyRegisterForm, MyUserForm
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
firewall = Security(app, user_datastore, register_form=MyRegisterForm)
admin = Admin(app, url='/', template_mode='bootstrap3', base_template='admin/my_base.html',
              index_view=AdminIndexView(url='/', name='Accueil'))


@app.context_processor
def security_context_processor():
    return dict(admin_base_template=admin.base_template, admin_view=admin.index_view, h=admin_helpers,
                get_url=admin_helpers.get_url)


from app.category import *
from app.friend import *
from app.meal import *
from app.recipe import *

admin.add_view(FriendView(db.session))
admin.add_view(CategoryView(db.session))
admin.add_view(MealView(db.session))
admin.add_view(RecipeView(db.session))


@app.route('/profile', endpoint='security.profile', methods=('GET',))
def profile():
    return render_template('firewall/profile.html')


@app.route('/settings', endpoint='security.settings', methods=('GET', 'POST'))
def settings():
    form = MyUserForm(request.form, obj=current_user)
    if request.method == 'POST' and form.validate():
        form.populate_obj(current_user)
        db.session.commit()
        flash('Nom et Prénom changés'.decode('utf-8'))
        return redirect(url_for('security.profile'))
    return render_template('firewall/settings.html', settings_form=form)
