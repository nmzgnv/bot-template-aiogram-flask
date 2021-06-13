## Telegram bot template
Template for creating scalable bots with aiogram

### What's in the template?
* Admin panel with the ability to view/edit/delete the database + analytics charts + ability to edit texts used in the bot + bot total control 
* All necessary directories for bot development  
* Basic database tables (ORM)

### Development
#### Technologies
* Python 3.8
* Aiogram
* Flask
* SQLAlchemy
* multiprocessing

#### Project structure
* bot
    * filters
    * handlers
    * keyboards
    * middlewares
    * states
    * utils
    * texts
* server (admin part)
    * model_views
    * templates
* database
    * models
    
Application package is in `server/main.py`


#### TODO
Change flask-sqlalchemy to async sqlalchemy

