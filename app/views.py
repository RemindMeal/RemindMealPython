from flask import url_for
from flask.ext.admin import expose
from app.entity import *
from flask.ext.admin.contrib.sqla import ModelView


class MyView(ModelView):
    can_view_details = True
    create_modal = True
    edit_modal = True
    details_modal = True

class CategoryView(MyView):

    column_list = ('name',)
    column_labels = dict(name='Nom')
    form_columns = ('name',)
    column_editable_list = ('name', 'date')
    can_edit = False

    create_modal_template = 'category/modals/create.html'
    details_modal_template = 'category/modals/details.html'

    def __init__(self, session):
        super(CategoryView, self).__init__(Category, session, 'Categories')


class FriendView(MyView):

    column_list = ('nom',)
    column_labels = dict(name='Prenom', surname='Nom')
    column_searchable_list = ('name', 'surname')
    form_excluded_columns = ('date',)

    column_formatters = dict(nom=lambda v, c, m, p: u'<a href="{:s}">{:s} {:s}</a>'.format(
        url_for('.show_view', id=m.id), m.name, m.surname))

    show_template = 'friend/show.html'

    def __init__(self, session):
        super(FriendView, self).__init__(Friend, session, "Amis")

    @expose('/show/<int:id>')
    def show_view(self, id):
        """
            Show model view.
        """

        return self.render(
            self.show_template,
            friend=Friend.query.get(id),
        )


class MealView(MyView):

    column_list = ('date', 'recipes', 'friends')
    column_labels = dict(date='Date', recipes='Menu', friends='Invites')
    column_filters = ('date', 'recipes', 'friends')

    create_modal_template = 'meal/modals/create.html'
    edit_modal_template = 'meal/modals/edit.html'
    details_modal_template = 'meal/modals/details.html'

    def __init__(self, session):
        super(MealView, self).__init__(Meal, session, "Repas")


class RecipeView(MyView):

    column_list = ('name', 'category')
    column_labels = dict(name='Nom', category='Categorie')
    column_filters = ('name', 'category.name')
    column_sortable_list = ('name', 'category.name')
    form_excluded_columns = ('date', 'meals')

    show_template = "recipe/show.html"

    create_modal_template = 'recipe/modals/create.html'
    edit_modal_template = 'recipe/modals/edit.html'
    details_modal_template = 'recipe/modals/details.html'

    def __init__(self, session):
        super(RecipeView, self).__init__(Recipe, session, "Recettes")

    @expose('/show/<int:id>')
    def show_view(self, id):
        """
            Show model view.
        """

        return self.render(self.show_template, recipe=Recipe.query.get(id))