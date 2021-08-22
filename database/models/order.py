import datetime

from database.loader import db
from sqlalchemy import Column, Integer, DateTime, ForeignKey


class Order(db.Model):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)

    product_id = Column(Integer, ForeignKey('product.id'))
    was_created = Column(DateTime(), default=datetime.datetime.now())

    user_id = Column(Integer, ForeignKey('user.id'))

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'{self.user.alias if self.user else ""} {self.product}'

    def __repr__(self):
        return self.__str__()
