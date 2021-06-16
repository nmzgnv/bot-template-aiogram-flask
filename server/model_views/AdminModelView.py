from flask_login import current_user

from database.models import AdminUser
from server.model_views.mixins.AuthMixin import AuthMixin
from flask_admin.contrib.sqla import ModelView


class AdminModelView(AuthMixin, ModelView):
    form_excluded_columns = ('password',)
    column_exclude_list = ('password',)

    def __init__(self, session, **kwargs):
        super(AdminModelView, self).__init__(AdminUser, session, **kwargs)

    @property
    def can_create(self):
        return current_user.is_super_admin

    @property
    def can_edit(self):
        return current_user.is_super_admin

    @property
    def can_delete(self):
        return current_user.is_super_admin and AdminUser.query.filter_by(is_super_admin=True).count() > 1
