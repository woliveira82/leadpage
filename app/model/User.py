from app import db


class User(db.Model):
    
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), nullable=False)
    recovery_email = db.Column(db.String(128), nullable=True)
    password = db.Column(db.String(128), nullable=False)
    old_password = db.Column(db.String(128), nullable=True)
    first_name = db.Column(db.String(128), nullable=False)
    last_name = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.Date, nullable=False, default=db.func.now())
    is_logged = db.Column(db.Boolean, nullable=False)
    is_active = db.Column(db.Boolean, nullable=False)
    image = db.Column(db.String(255), nullable=True)
    campaign_list = db.relationship('Campaign', lazy=True)


    @classmethod
    def create(cls, email, password, first_name, recovery_email=None, last_name=None, image=None):
        user_data = {
            'email': email,
            'recovery_email': recovery_email,
            'password': '*****',
            'old_password': None,
            'first_name': first_name,
            'last_name': last_name,
            'created_at': None,
            'is_logged': False,
            'is_active': True,
            'image': image,
        }
        user = cls(**user_data)
        db.session.add(user)
        db.session.commit()
        return user


    def save(self):
        db.session.add(self)
        db.session.commit()


    def to_dict(self):
        user = {
            'id': self.id,
            'email': self.email,
            'recovery_email': self.recovery_email,
            'password': '*****',
            'old_password': '*****',
            'first_name': self.first_name,
            'last_name': self.last_name,
            'created_at': self.created_at,
            'is_logged': self.is_logged,
            'is_active': self.is_active,
            'image': self.image,
        }
        return user
