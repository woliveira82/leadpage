from app import db


class Lead(db.Model):
    
    __tablename__ = 'lead'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), nullable=False)
    first_name = db.Column(db.String(128), nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.now())
    

    @classmethod
    def create(cls, email, first_name=None):
        lead_data = {
            'email': email,
            'first_name': first_name,
        }
        lead = cls(**lead_data)
        db.session.add(lead)
        db.session.commit()
        return lead


    def save(self):
        db.session.add(self)
        db.session.commit()


    def to_dict(self):
        lead = {
            'id': self.id,
            'email': self.email,
            'first_name': self.first_name,
            'created_at': self.created_at,
        }
        return lead
