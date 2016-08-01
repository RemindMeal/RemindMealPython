from app.views import MyView
from flask import url_for, Blueprint, render_template
from flask_admin import expose
from .model import Friend

friend = Blueprint('friend', __name__)


@friend.route('/', endpoint='list', methods=('GET',))
def friend_list():
    return render_template('friend/list.html')


class FriendView(MyView):

    column_list = ('nom',)
    column_labels = dict(name='Prenom', surname='Nom')
    column_searchable_list = ('name', 'surname')
    form_excluded_columns = ('date', 'meals', 'user')

    column_formatters = dict(nom=lambda v, c, m, p: u'<a href="{:s}">{:s} {:s}</a>'.format(
        url_for('.show_view', id=m.id), m.name, m.surname))

    create_modal_template = 'friend/modals/create.html'
    details_modal_template = 'friend/modals/details.html'
    edit_modal_template = 'friend/modals/edit.html'

    show_template = 'friend/show.html'

    def __init__(self, session):
        super(FriendView, self).__init__(Friend, session, "Amis")

    @expose('/show/<int:id>')
    def show_view(self, id):
        return self.render(self.show_template, friend=Friend.query.get(id))
