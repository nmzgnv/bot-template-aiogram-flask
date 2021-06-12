from flask_admin import BaseView, expose


class BotSettingsView(BaseView):
    @expose('/')
    def index(self):
        return self.render('bot_settings_view.html')