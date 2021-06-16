from flask import url_for
from flask_login import current_user
from werkzeug.utils import redirect


class AuthMixin(object):
    def is_accessible(self):
        if current_user.is_authenticated:
            return True
        return False

    def _handle_view(self, name, **kwargs):
        if not self.is_accessible():
            return redirect(url_for('auth.login'))
