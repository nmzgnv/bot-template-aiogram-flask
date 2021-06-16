from flask_login import UserMixin
from werkzeug.security import generate_password_hash

from database.loader import db
from sqlalchemy import Column, Integer, String, Boolean


class AdminUser(UserMixin, db.Model):
    """
        Admin panel authentication model
    """
    id = Column(Integer, primary_key=True)
    email = Column(String(100), unique=True)
    password = Column(String(100))
    name = Column(String(100))
    is_super_admin = Column(Boolean(), default=False)

    @staticmethod
    def register(email, name, password, is_super_admin=False):
        new_user = AdminUser(email=email, password=generate_password_hash(password, method='sha256'),
                             is_super_admin=is_super_admin, name=name)
        db.session.add(new_user)
        db.session.commit()
        return new_user
