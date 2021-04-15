from app import db


class Email(db.Model):
    
    __tablename__ = 'email'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    body = db.Column(db.Text, nullable=False)
    action = db.Column(db.Integer, db.ForeignKey('action.id'), nullable=True)
    campaign_id = db.Column(db.Integer, db.ForeignKey('campaign.id'), nullable=False)


    @classmethod
    def create(cls, title, body, action=None):
        #Get campaign_id from session
        campaign_id
        email_data = {
            'title': title,
            'body': body,
            'action': action,
            'campaign_id': campaign_id,
        }
        email = cls(**email_data)
        db.session.add(email)
        db.session.commit()
        return email


    def save(self):
        db.session.add(self)
        db.session.commit()


    def to_dict(self):
        email = {
            'id': self.id,
            'title': self.title,
            'body': self.body,
            'action': self.action,
            'campaign_id': self.campaign_id,
        }
        return email
