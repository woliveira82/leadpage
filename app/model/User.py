from app import db
from .Dao import Dao
from datetime import datetime


class User(db.Model, Dao):
    
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), nullable=False)
    recovery_email = db.Column(db.String(128), nullable=True)
    password = db.Column(db.String(128), nullable=False)
    old_password = db.Column(db.String(128), nullable=True)
    first_name = db.Column(db.String(128), nullable=False)
    last_name = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.Date, nullable=False)
    is_logged = db.Column(db.Boolean, nullable=False)
    is_active = db.Column(db.Boolean, nullable=False)
    image = db.Column(db.String(255), nullable=True)


    def __init__(self, email, password, first_name, recovery_email=None, old_password=None, last_name=None, created_at=None, is_logged=None, is_active=None, image=None, id=None):
        self.id = id
        self.email = email
        self.recovery_email = recovery_email
        self.password = password
        self.old_password = old_password
        self.first_name = first_name
        self.last_name = last_name
        self.created_at = created_at if created_at else datetime.now()
        self.is_logged = is_logged
        self.is_active = is_active
        self.image = image
    