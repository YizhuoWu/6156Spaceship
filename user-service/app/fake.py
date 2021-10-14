from faker import Faker
from .models import User
from hashlib import md5
from . import db


faker = Faker()
md5 = md5()


def users(count=100):
    for i in range(count):
        us = User(
            username=faker.user_name(),
            hashed_passwd=random_hashed_passwd(),
            address=faker.address()
        )
        db.session.add(us)
    db.session.commit()


def random_hashed_passwd():
    s = faker.pystr()
    md5.update(s.encode('utf-8'))
    return md5.hexdigest()

