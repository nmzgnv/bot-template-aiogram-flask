from sqlalchemy import Column, Integer, String

from database.loader import db


class Texts(db.Model):
    __tablename__ = 'texts'
    id = Column(Integer, primary_key=True)

    name = Column(String(length=80), nullable=False)
    value = Column(db.UnicodeText)

    def __init__(self, name, value="empty text"):
        self.name = name
        self.value = value


if __name__ == '__main__':
    db.create_all()
    db.session.commit()
