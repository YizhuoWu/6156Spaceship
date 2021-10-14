import unittest
from app.models import User


class ModelTestCase(unittest.TestCase):
    def test_to_json(self):
        user_json = {
            'links': [
                {'rel': 'self', 'url': '/fake/url'},
                {'rel': 'self', 'url': '/fake/url'},
            ]
        }
        print(user_json)
