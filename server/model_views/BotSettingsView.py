from flask_admin import BaseView, expose

from server.model_views.mixins.AuthMixin import AuthMixin


class BotSettingsView(AuthMixin, BaseView):
    @expose('/')
    def index(self):
        return self.render('bot_settings_view.html')
