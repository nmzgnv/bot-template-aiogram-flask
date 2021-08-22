import datetime

from sqlalchemy import Column, Integer, String, Boolean, DateTime, and_
from sqlalchemy.orm import relationship

from database.loader import db


class User(db.Model):
    id = Column(Integer, primary_key=True)

    telegram_id = Column(String(40), unique=True)
    chat_id = Column(String(40))

    alias = Column(String(40))

    referer_id = Column(String(40))
    is_banned = Column(Boolean)

    state = Column(String(50), default=None, nullable=True)
    state_data = Column(String(1000), default=None, nullable=True)

    balance = Column(Integer, default=0)
    orders = relationship("Order", backref='user')
    was_registered = Column(DateTime, default=datetime.datetime.now())

    def __init__(self, telegram_id, alias, referer_id='', chat_id=''):
        self.telegram_id = str(telegram_id)
        self.chat_id = str(chat_id)
        self.alias = alias
        self.referer_id = referer_id
        self.orders = []
        self.is_banned = False
        self.balance = 0

    def __repr__(self):
        return f'{self.alias} : {self.telegram_id}'

    def get_registration_date(self):
        return self.was_registered.date()

    @staticmethod
    def register(telegram_user, chat_id, referer_id=''):
        if not User.query.filter_by(telegram_id=str(telegram_user.id)).first():
            if not User.query.filter_by(telegram_id=referer_id).first():
                referer_id = ''

            db.session.add(User(telegram_user.id, telegram_user.username, referer_id=referer_id, chat_id=chat_id))
            db.session.commit()

    @staticmethod
    def get(user_id: str = '', chat_id: str = ''):
        user = User.query.filter(and_(User.telegram_id == user_id, User.chat_id == chat_id)).first()

        if not user:
            ValueError('User does not exist')

        return user
