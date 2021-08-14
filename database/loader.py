import logging
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from database.db_config import Config

# TODO change db to async

templates_folder = os.path.abspath('./server/templates')
logging.info(f"Admin templates folder: {templates_folder}")
app = Flask(__name__, template_folder=templates_folder, static_folder=templates_folder + '/static', )
app.config.from_object(Config)
db = SQLAlchemy(app)

if __name__ == '__main__':
    # db.drop_all()
    db.create_all()
    db.session.commit()
