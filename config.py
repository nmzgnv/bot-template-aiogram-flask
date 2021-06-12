import os

DEBUG = os.getenv('DEBUG', False)
USE_LOCAL_VARIABLES = os.getenv('USE_LOCAL_VARIABLES', True)

# bot
BOT_TOKEN = os.getenv('BOT_TOKEN')
ADMINS = [492621220]

# server
PORT = int(os.environ.get("PORT", 5000))
PRODUCTION_HOST = '0.0.0.0'
LOCAL_HOST = '127.0.0.1'

# database
LOCAL_DATABASE_URL = 'sqlite:///Main.db'
DATABASE_URL = os.getenv('DATABASE_URL')