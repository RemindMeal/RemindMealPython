from app.entity import Friend, Meal
from flask.ext.admin.contrib.sqla import ModelView

class FriendView(ModelView):

    def __init__(self, session):
        super(FriendView, self).__init__(Friend, session)


class MealView(ModelView):

    def __init__(self, session):
        super(MealView, self).__init__(Meal, session)
