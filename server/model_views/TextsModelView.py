import flask
import requests
from loguru import logger

from .CKEditorModelView import CKEditorModelView
from .mixins.AuthMixin import AuthMixin


class TextsModelView(AuthMixin, CKEditorModelView):
    def after_model_change(self, form, model, is_created):
        if not is_created:  # Model was updated
            try:
                ans = requests.post(flask.request.url_root + 'restart_bot')
                logger.info(ans.text)
            except Exception as error:
                logger.error(f"Bot restart error: {error}")
