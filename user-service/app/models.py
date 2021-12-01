from . import db
from flask import url_for


class User(db.Model):
    __tablename__ = 'users'

    username = db.Column(db.String(32), index=True, unique=True)
    hashed_passwd = db.Column(db.String(128))
    address = db.Column(db.String(128))
    state = db.Column(db.String(20))
    city = db.Column(db.String(20))
    phone_number = db.Column(db.String(20))
    email = db.Column(db.String(40), primary_key=True, index=True)

    def __str__(self):
        return 'username={}, hashed_passwd={}, address={}'.format(self.username, self.hashed_passwd, self.address)

    def to_json(self):
        return {
            'email': self.email,
            'username': self.username,
            'state': self.state,
            'city': self.city,
            'address': self.address,
            'links': [
                {'rel': 'self', 'url': url_for('api.get_user_profile_by_username', username=self.username)}
            ]
        }
