from app.entity import Category, Friend, Meal
from flask.ext.admin.contrib.sqla import ModelView

class CategoryView(ModelView):

    def __init__(self, session):
        super(CategoryView, self).__init__(Category, session)


class FriendView(ModelView):

    def __init__(self, session):
        super(FriendView, self).__init__(Friend, session)


class MealView(ModelView):

    def __init__(self, session):
        super(MealView, self).__init__(Meal, session)
