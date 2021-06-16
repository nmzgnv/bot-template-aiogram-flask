import logging

import flask
from .CKEditorModelView import CKEditorModelView
import requests

from .mixins.AuthMixin import AuthMixin


class TextsModelView(AuthMixin, CKEditorModelView):
    def after_model_change(self, form, model, is_created):
        if not is_created:  # Model was updated
            try:
                ans = requests.post(flask.request.url_root + 'restart_bot')
                logging.info(ans.text)
            except Exception as error:
                logging.error(f"Bot restart error: {error}")
