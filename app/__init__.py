from flask import Flask, flash, redirect, render_template, request, url_for
from flask_admin import helpers as admin_helpers
from flask_babelex import Babel
from flask_debugtoolbar import DebugToolbarExtension
from flask_login import current_user
from flask_migrate import Migrate
from flask_security import SQLAlchemyUserDatastore, Security

app = Flask(__name__)
app.config.from_object('config')

from app.utils import date
app.jinja_env.filters['date'] = date
app.jinja_env.autoescape = False
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

DebugToolbarExtension(app)
Babel(app, default_locale='fr')
# Sentry(app)

from app.models import db, Category

db.init_app(app)
Migrate(app, db)


from app.forms import MyRegisterForm, MyUserForm
from app.models import User, Role
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
firewall = Security(app, user_datastore, register_form=MyRegisterForm)

from app.views import admin
admin.init_app(app)


@app.context_processor
def security_context_processor():
    return dict(admin_base_template=admin.base_template, admin_view=admin.index_view, h=admin_helpers,
                get_url=admin_helpers.get_url)


@app.route('/profile', endpoint='security.profile', methods=('GET',))
def profile():
    return render_template('firewall/profile.html')


@app.route('/settings', endpoint='security.settings', methods=('GET', 'POST'))
def settings():
    form = MyUserForm(request.form, obj=current_user)
    if request.method == 'POST' and form.validate():
        if form.name.data != current_user.name or form.surname.data != current_user.surname:
            form.populate_obj(current_user)
            db.session.commit()
            flash('Nom et Prénom changés')
        return redirect(url_for('security.profile'))
    return render_template('firewall/settings.html', settings_form=form)

if __name__ == '__main__':
    app.run()
