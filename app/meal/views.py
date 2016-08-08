from flask import Blueprint, render_template

from app import db
from app.recipe.model import Recipe
from app.utils import MyQueryAjaxModelLoader
from app.views import MyView
from .model import Meal

meal = Blueprint('meal', __name__, template_folder='.templates')


@meal.route('/', endpoint='list', methods=('GET', 'POST'))
def meal_list():
    return render_template('meal/list.html', meals=Meal.query.all())


class MealView(MyView):

    column_list = ('date', 'recipes', 'friends')
    column_labels = dict(date='Date', recipes='Menu', friends='Invites')
    column_filters = ('date', 'recipes', 'friends')
    column_searchable_list = ('date', 'recipes.name', 'friends.name', 'friends.surname')
    form_excluded_columns = ('user',)

    create_modal_template = 'meal/modals/create.html'
    edit_modal_template = 'meal/modals/edit.html'
    details_modal_template = 'meal/modals/details.html'

    form_ajax_refs = {
        "recipes": MyQueryAjaxModelLoader(
            "recipes", db.session, Recipe, fields=['name']
        ),
    }

    def __init__(self, session):
        super(MealView, self).__init__(Meal, session, "Repas")

