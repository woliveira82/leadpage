from app import db


class Action(db.Model):

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(128), nullable=False)
    id_campaign = db.Column(db.Integer, db.ForeignKey('campaign.id'), nullable=False)


    @classmethod
    def create(cls, name):
        id_campaign #get id_campaign in session
        action_data = {
            'name': name,
            'id_campaign': id_campaign,
        }
        action = cls(**name)
        db.session.add(name)
        db.session.commit()

    
    def save(self):
        db.session.add(self)
        db.session.commit()

    
    def to_dict(self):
        action = {
            'id': self.id,
            'name': self.name,
            'id_campaign': self.id_campaign,
        }
        return action