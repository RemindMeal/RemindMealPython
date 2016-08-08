from flask_security import RegisterForm
from wtforms import Form, StringField, SubmitField


class MyUserForm(Form):
    name = StringField()
    surname = StringField()
    submit = SubmitField()


class MyRegisterForm(RegisterForm, MyUserForm):
    pass