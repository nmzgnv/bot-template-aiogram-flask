import datetime

from database.loader import db
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship


class User(db.Model):
    id = Column(Integer, primary_key=True)

    telegram_id = Column(String(40), unique=True)
    alias = Column(String(40))

    referer_id = Column(String(40))
    is_banned = Column(Boolean)
    state = Column(Integer, default=None, nullable=True)

    balance = Column(Integer, default=0)
    orders = relationship("Order", backref='user')
    was_registered = Column(DateTime, default=datetime.datetime.now())

    def __init__(self, telegram_id, alias, referer_id=''):
        self.telegram_id = str(telegram_id)
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
    def register(telegram_user, referer_id=''):
        if not User.query.filter_by(telegram_id=str(telegram_user.id)).first():
            if not User.query.filter_by(telegram_id=referer_id).first():
                referer_id = ''

            db.session.add(User(telegram_user.id, telegram_user.username, referer_id=referer_id))
            db.session.commit()
