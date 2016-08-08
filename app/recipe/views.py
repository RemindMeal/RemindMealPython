from flask import Blueprint, render_template
from flask_admin import expose

from app import db
from app.category.model import Category
from app.utils import MyQueryAjaxModelLoader
from app.views import MyView
from .model import Recipe

recipe = Blueprint('recipe', __name__)


@recipe.route('/', endpoint='list', methods=('GET',))
def recipe_list():
    return render_template('recipe/list.html', recipes=Recipe.query.all())


@recipe.route('/create', endpoint='create', methods=('POST',))
def recipe_create():
    pass


class RecipeView(MyView):

    column_list = ('name', 'category', 'mark', 'description', 'reference')
    column_labels = dict(name='Nom', category='Categorie', mark='Note')
    column_filters = ('name', 'category.name', 'description')
    column_searchable_list = ('name', 'category.name', 'description')
    column_sortable_list = ('name', 'category.name')
    form_columns = ('name', 'category', 'mark', 'description', 'reference')

    show_template = "recipe/show.html"

    create_modal_template = 'recipe/modals/create.html'
    edit_modal_template = 'recipe/modals/edit.html'
    details_modal_template = 'recipe/modals/details.html'

    form_ajax_refs = {
        "category": MyQueryAjaxModelLoader(
            "category", db.session, Category, fields=['name']
        ),
    }

    def __init__(self, session):
        super(RecipeView, self).__init__(Recipe, session, "Recettes")

    @expose('/show/<int:id>')
    def show_view(self, id):
        return self.render(self.show_template, recipe=Recipe.query.get(id))
