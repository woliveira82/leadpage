from app import db


class Campaign(db.Model):
    
    __tablename__ = 'campaign'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    is_active = db.Column(db.Boolean, nullable=False, default=True)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.now())
    auto_deactivation = db.Column(db.DateTime, nullable=True)
    auto_activation = db.Column(db.DateTime, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    

    @classmethod
    def create(cls, name, user_id, description=None):
        campaign_data = {
            'name': name,
            'description': description,
            'is_active': True,
            'user_id': user_id
        }
        campaign = cls(**campaign_data)
        db.session.add(campaign)
        db.session.commit()
        return campaign
    

    def save(self):
        db.session.add(self)
        db.session.commit()
    

    def to_dict(self):
        campaign = {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'is_active': self.is_active,
            'created_at': self.created_at,
            'auto_deactivation': self.auto_deactivation,
            'auto_activation': self.auto_activation,
            'user_id': self.user_id,
        }
        return campaign