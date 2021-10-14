from . import db
from flask import url_for


class User(db.Model):
    __tablename__ = 'users'
    username = db.Column(db.String(32), primary_key=True, index=True)
    hashed_passwd = db.Column(db.String(128))
    address = db.Column(db.String(128))

    def __str__(self):
        return 'username={}, hashed_passwd={}, address={}'.format(self.username, self.hashed_passwd, self.address)

    def to_json(self):
        return {
            'username': self.username,
            'address': self.address,
            'links': [
                {'rel': 'self', 'url': url_for('api.get_user_info', username=self.username)},
            ]
        }
