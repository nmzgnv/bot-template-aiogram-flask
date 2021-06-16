from flask_admin.contrib.sqla import ModelView

from database.models import Order
from server.model_views.mixins.AuthMixin import AuthMixin


class OrderModelView(AuthMixin, ModelView):
    form_excluded_columns = ('product_id')

    def __init__(self, session, **kwargs):
        super(OrderModelView, self).__init__(Order, session, **kwargs)
