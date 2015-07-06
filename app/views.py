from app.entity import Meal
from flask.ext.admin.contrib.sqla import ModelView

class MealView(ModelView):

    def __init__(self, session):
        super(MealView, self).__init__(Meal, session)
