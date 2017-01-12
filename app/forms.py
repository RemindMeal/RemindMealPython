from flask_admin.model.form import InlineFormAdmin
from flask_login import current_user
from flask_security import RegisterForm
from wtforms import Form, StringField, SubmitField


class MyUserForm(Form):
    name = StringField()
    surname = StringField()
    submit = SubmitField()


class MyRegisterForm(RegisterForm, MyUserForm):
    pass


class InlineFriendForm(InlineFormAdmin):
    form_columns = ('id', 'name', 'surname')
    form_args = dict(name=dict(label='Nom'), surname=dict(label='Prénom'))

    def on_model_change(self, form, model, is_created):
        model.user = current_user
