from datetime import datetime

from app import db

from . import Dao


class Leads(db.Model, Dao):
    
    __tablename__ = 'leads'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), nullable=False)
    first_name = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.now())
    is_active = db.Column(db.Boolean, nullable=False, default=True)
    extra_conf = db.Column(db.Text, nullable=True)
    

    def __init__(self, email, first_name, created_at=None, is_active=None, extra_conf=None, id=None):
        self.id = id
        self.email = email
        self.first_name = first_name
        self.created_at = created_at
        self.is_active = is_active
        self.extra_conf = extra_conf
