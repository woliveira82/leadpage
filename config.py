import os.path

def sqlite_path():
    sqlite_path = os.path.dirname(os.path.abspath(__file__))
    return sqlite_path

ENV = 'production'
DEBUG = False
SQLALCHEMY_DATABASE_URI = f'sqlite:///{sqlite_path()}storage.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
JWT_SECRET_KEY = 'super-secret'