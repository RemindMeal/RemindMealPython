from flask_admin.contrib.sqla import ModelView
from flask_security import current_user


class MyView(ModelView):
    can_view_details = True
    create_modal = True
    edit_modal = True
    details_modal = True
    form_excluded_columns = ('user',)

    def is_accessible(self):
        return current_user.is_authenticated

    def get_query(self):
        return super(MyView, self).get_query().filter(self.model.user == current_user)

    def get_count_query(self):
        return super(MyView, self).get_count_query().filter(self.model.user == current_user)

    def on_model_change(self, form, model, is_created):
        model.user = current_user
