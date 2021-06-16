from flask_admin.contrib.sqla import ModelView

from server.model_views.mixins.AuthMixin import AuthMixin


class HiddenModelView(AuthMixin, ModelView):

    def is_visible(self):
        return False

    def __init__(self, model, session, **kwargs):
        super(HiddenModelView, self).__init__(model, session, **kwargs)