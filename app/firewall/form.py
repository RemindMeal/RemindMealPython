from flask_security import RegisterForm
from wtforms import StringField


class MyRegisterForm(RegisterForm):
    name = StringField()
    surname = StringField()
