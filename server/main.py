import logging
import multiprocessing
import os

from flask_admin import Admin
from flask import redirect, request, make_response
from flask_admin.contrib.sqla import ModelView
from flask_ckeditor import CKEditor

from bot.main import bot_init
from config import PORT, USE_LOCAL_VARIABLES, LOCAL_HOST, PRODUCTION_HOST

from daemon import daemon_init
from database.loader import app, db
from database.models import User, Texts, Order, Product
from server.model_views import (CKEditorModelView, BotSettingsView, HiddenModelView)
from server.model_views.HomeView import HomeView

telegram_bot = multiprocessing.Process(target=bot_init)
daemon = multiprocessing.Process(target=daemon_init)
daemon.daemon = True

ckeditor = CKEditor(app)


@app.route('/')
def start_page():
    return redirect('/admin')


@app.route('/change_token', methods=['POST'])
def change_token():
    new_token = request.form.get('token')
    logging.info("bot token changed")
    os.environ["BOT_TOKEN"] = new_token
    return make_response({'result': 'success'}, 200)


@app.route('/get_current_bot_token', methods=['GET'])
def get_current_token():
    token = os.getenv('BOT_TOKEN', 'None')
    return make_response({'token': token}, 200)


def stop_bot_process():
    global telegram_bot
    telegram_bot.terminate()
    telegram_bot.kill()
    logging.info(f"Bot is off")


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
    logging.info(f"Telegram bot was launched")
    return make_response({'result': 'success'}, 200)


def run_modules():
    global telegram_bot, daemon
    jobs = [telegram_bot, daemon]

    telegram_bot.start()
    daemon.start()


def init_admin_panel():
    admin = Admin(app, name='bot config', template_mode='bootstrap3')

    admin.add_view(HomeView(name='Home', menu_icon_type='glyph', menu_icon_value='glyphicon-home'))
    admin.add_view(ModelView(User, db.session, name='Users'))
    admin.add_view(ModelView(Order, db.session, name='Orders'))
    admin.add_view(ModelView(Product, db.session, name='Products'))
    admin.add_view(BotSettingsView(name='Main', endpoint='bot_settings', category='Bot settings'))
    admin.add_view(CKEditorModelView(Texts, db.session, category='Bot settings'))


def init_server():
    db.create_all()
    db.session.commit()

    init_admin_panel()

    app.secret_key = 'secret'
    app.config['SESSION_TYPE'] = 'filesystem'
    host = LOCAL_HOST if USE_LOCAL_VARIABLES else PRODUCTION_HOST

    run_modules()
    app.run(host=host, port=PORT, use_reloader=False)  # use_reloader=False to avoid conflict with multiprocessing


if __name__ == '__main__':
    init_server()
