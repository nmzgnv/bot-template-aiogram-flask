import pathlib
import sys

sys.path.insert(0, str(pathlib.Path().resolve()).split('\server')[0])

from loguru import logger
import multiprocessing
import os

from flask_admin import Admin
from flask import redirect, request, make_response
from flask_admin.contrib.sqla import ModelView
from flask_ckeditor import CKEditor
from flask_login import LoginManager
from flask_migrate import Migrate

from bot.main import bot_init
from config import PORT, USE_LOCAL_VARIABLES, LOCAL_HOST, PRODUCTION_HOST, BOT_TOKEN, ADMIN_EMAIL, ADMIN_PASSWORD

from daemon import daemon_init
from database.loader import app, db
from database.models import User, Texts, Order, Product, AdminUser
from server.model_views import BotSettingsView
from server.model_views.AdminConfig import Categories
from server.model_views.AdminModelView import AdminModelView
from server.model_views.HomeView import HomeView
from server.model_views.TextsModelView import TextsModelView
from server.auth import auth as auth_blueprint

logger.add("debug.log", format='{time} {level} {message}', level="DEBUG", rotation="00:00", compression="zip")

telegram_bot = multiprocessing.Process(target=bot_init)
daemon = multiprocessing.Process(target=daemon_init)
daemon.daemon = True

ckeditor = CKEditor(app)
migrate = Migrate(app, db)


@app.route('/')
def start_page():
    return redirect('/admin')


@app.route('/change_token', methods=['POST'])
def change_token():
    new_token = request.form.get('token')
    os.environ["BOT_TOKEN"] = new_token
    logger.info("Bot token was changed. Restarting the bot...")
    restart_bot()
    return make_response({'result': 'success'}, 200)


@app.route('/get_current_bot_token', methods=['GET'])
def get_current_token():
    token = str(BOT_TOKEN)
    return make_response({'token': token}, 200)


def stop_bot_process():
    global telegram_bot
    telegram_bot.terminate()
    telegram_bot.kill()
    logger.info(f"Bot is off")


@app.route('/stop_bot', methods=['POST'])
def stop_bot():
    stop_bot_process()
    return make_response({'result': 'success'}, 200)


@app.route('/restart_bot', methods=['POST'])
def restart_bot():
    global telegram_bot
    stop_bot_process()
    telegram_bot = multiprocessing.Process(target=bot_init)
    telegram_bot.start()
    logger.info(f"Bot was launched")
    return make_response({'result': 'success'}, 200)


def run_modules():
    global telegram_bot, daemon
    jobs = [telegram_bot, daemon]

    telegram_bot.start()
    daemon.start()


def init_admin_panel():
    admin = Admin(app, name='Admin panel', template_mode='bootstrap3',
                  index_view=HomeView(name='Home', menu_icon_type='glyph', menu_icon_value='glyphicon-home'))

    admin.add_view(ModelView(User, db.session, name='Users'))
    admin.add_view(ModelView(Order, db.session, name='Orders'))
    admin.add_view(ModelView(Product, db.session, name='Products'))
    admin.add_view(AdminModelView(db.session, category=Categories.MANAGEMENT))
    admin.add_view(BotSettingsView(name='Bot', endpoint='bot_settings', category=Categories.MANAGEMENT))
    admin.add_view(TextsModelView(Texts, db.session, category=Categories.MANAGEMENT))


def init_server():
    db.create_all()
    db.session.commit()

    init_admin_panel()

    app.secret_key = 'secret'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.register_blueprint(auth_blueprint)
    host = LOCAL_HOST if USE_LOCAL_VARIABLES else PRODUCTION_HOST

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return AdminUser.query.get(int(user_id))

    if AdminUser.query.count() == 0:
        AdminUser.register(ADMIN_EMAIL, 'admin', ADMIN_PASSWORD, is_super_admin=True)

    run_modules()
    app.run(host=host, port=PORT, use_reloader=False)  # use_reloader=False to avoid conflict with multiprocessing


if __name__ == '__main__':
    init_server()
