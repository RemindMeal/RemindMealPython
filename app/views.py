from flask import url_for
from flask_admin import Admin, AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView
from flask_admin.contrib.sqla.filters import FilterGreater, FilterLike, FilterSmaller
from flask_admin.model.filters import BaseDateFilter
from flask_admin.model.template import TemplateLinkRowAction
from flask_security import current_user

from app import db
from app.models import Category, Friend, Meal, Recipe
from app.utils import MyQueryAjaxModelLoader


class MyUserView(ModelView):
    can_view_details = True
    create_modal = True
    edit_modal = True
    details_modal = True
    form_excluded_columns = ('user',)

    def is_accessible(self):
        return current_user.is_authenticated

    def get_query(self):
        return super(MyUserView, self).get_query().filter(self.model.user == current_user)

    def get_count_query(self):
        return super(MyUserView, self).get_count_query().filter(self.model.user == current_user)

    def on_model_change(self, form, model, is_created):
        model.user = current_user


class MyAdminView(ModelView):

    def is_accessible(self):
        return current_user.is_authenticated and current_user.has_role('admin')


class CategoryView(MyAdminView):

    column_list = ('name',)
    column_labels = dict(name='Nom')
    form_columns = ('name',)
    column_editable_list = ('name', )
    can_edit = False

    create_modal_template = 'category/modals/create.html'
    details_modal_template = 'category/modals/details.html'

    def __init__(self, session):
        super(CategoryView, self).__init__(Category, session, u'Catégories')


class MyEditPopupRowAction(TemplateLinkRowAction):
    def __init__(self):
        super(MyEditPopupRowAction, self).__init__('row_actions.my_edit_row_popup')


class FriendView(MyUserView):

    # Index view
    list_template = 'friend/list.html'
    column_list = ('nom',)
    column_labels = dict(name='Prénom', surname='Nom')
    column_searchable_list = ('name', 'surname')
    action_disallowed_list = ['delete']

    column_formatters = dict(nom=lambda v, c, m, p: u'<a href="{:s}">{:s} {:s}</a>'.format(
        url_for('.show_view', id=m.id), m.name, m.surname))

    # Details view
    details_modal_template = 'friend/modals/details.html'

    # Create view
    create_modal_template = 'friend/modals/create.html'
    form_columns = ('name', 'surname')

    # Edit view
    edit_modal_template = 'friend/modals/edit.html'

    show_template = 'friend/show.html'

    def __init__(self, session):
        super(FriendView, self).__init__(Friend, session, "Amis")

    @expose('/show/<int:id>')
    def show_view(self, id):
        return self.render(self.show_template, friend=Friend.query.get(id))


class RecipeView(MyUserView):

    # Index view
    column_list = ('name', 'category', 'description', 'reference')
    column_labels = dict(name='Nom', category='Catégorie', reference='Référence')
    column_filters = ('name', 'category.name', 'description')
    column_searchable_list = ('name', 'category.name', 'description')
    column_sortable_list = ('name', 'category.name')

    # Create view
    create_modal_template = 'recipe/modals/create.html'
    form_columns = ('name', 'category', 'description', 'reference')

    # Details view
    show_template = 'recipe/show.html'
    details_modal_template = 'recipe/modals/details.html'

    # Edit view
    edit_modal_template = 'recipe/modals/edit.html'

    def __init__(self, session):
        super(RecipeView, self).__init__(Recipe, session, "Recettes")

    @expose('/show/<int:id>')
    def show_view(self, id):
        return self.render(self.show_template, recipe=Recipe.query.get(id))


class RecipeFilter(FilterGreater, FilterSmaller,  BaseDateFilter):
    pass


class MealView(MyUserView):

    # List
    list_template = 'meal/list.html'
    column_list = ('date', 'recipes', 'friends')
    column_labels = dict(date='Date', recipes='Menu', friends='Invités')
    column_searchable_list = ('date', 'recipes.name', 'friends.name', 'friends.surname')
    action_disallowed_list = ['delete']
    column_filters = (
        'date',
        FilterLike(Recipe.name, name='Recette'),
        FilterLike(Friend.surname, name='Invité')
    )
    column_default_sort = 'date'

    # Details
    can_view_details = False

    # Create
    form_columns = ('recipes', 'friends', 'date')

    # inline_models = (InlineFriendForm(Friend), )
    create_modal_template = 'meal/modals/create.html'

    # Edit
    edit_modal_template = 'meal/modals/edit.html'

    form_ajax_refs = {
        "recipes": MyQueryAjaxModelLoader(
            "recipes", db.session, Recipe, fields=['name']
        ),
        "friends": MyQueryAjaxModelLoader(
            "friends", db.session, Friend, fields=['name']
        ),
    }

    def __init__(self, session):
        super(MealView, self).__init__(Meal, session, "Repas")


admin = Admin(url='/', template_mode='bootstrap3', base_template='admin/my_base.html',
              index_view=AdminIndexView(url='/', name='Accueil'))
admin.add_view(FriendView(db.session))
admin.add_view(CategoryView(db.session))
admin.add_view(MealView(db.session))
admin.add_view(RecipeView(db.session))
