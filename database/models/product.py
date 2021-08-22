from database.loader import db
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship


class Product(db.Model):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)

    name = Column(String(50))
    description = Column(String(200))
    weight = Column(Float)
    price = Column(Integer)
    available_quantity = Column(Integer, default=10)
    image_url = Column(String(200), nullable=True)

    orders = relationship('Order', backref='product')

    def __str__(self):
        return self.name
