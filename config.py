import os

DEBUG = os.getenv('DEBUG', 'False') == 'True'
USE_LOCAL_VARIABLES = os.getenv('USE_LOCAL_VARIABLES', 'True') == 'True'

# bot
BOT_TOKEN = os.getenv('BOT_TOKEN', "1288081852:AAGCA-YApnvE6nYaULjU1ejv7NSx8G7PvAY")
ADMINS = [492621220]

# server
PORT = int(os.environ.get("PORT", 5000))
PRODUCTION_HOST = '0.0.0.0'
LOCAL_HOST = '127.0.0.1'

# main admin data
ADMIN_EMAIL = os.getenv('ADMIN_PASSWORD', 'admin@admin')
ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD', 'admin')

# database
LOCAL_DATABASE_URL = 'sqlite:///Main.db'
DATABASE_URL = os.getenv('DATABASE_URL')
