# coding: utf-8

from app.views import MyView
from flask import Blueprint, render_template
from .model import Category

category = Blueprint('category', __name__)


@category.route('/', endpoint='list', methods=('GET',))
def category_list():
    return render_template('category/list.html', categories=Category.query.all())


class CategoryView(MyView):

    column_list = ('name',)
    column_labels = dict(name='Nom')
    form_columns = ('name',)
    column_editable_list = ('name', 'date')
    can_edit = False

    create_modal_template = 'category/modals/create.html'
    details_modal_template = 'category/modals/details.html'

    def __init__(self, session):
        super(CategoryView, self).__init__(Category, session, u'Catégories')
