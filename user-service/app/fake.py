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
            state=faker.state(),
            city=faker.city(),
            address=faker.address(),
            email=faker.first_name() + '.' + faker.last_name() + "@columbia.edu",
            phone_number=faker.phone_number(),
        )
        db.session.add(us)
        try:
            db.session.commit()
        except:
            db.session.rollback()


def random_hashed_passwd():
    s = faker.pystr()
    md5.update(s.encode('utf-8'))
    return md5.hexdigest()
