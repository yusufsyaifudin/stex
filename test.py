#!/bin/python
import unittest

from app import db
from app.home_module.models.user import User


class TestCase(unittest.TestCase):

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_insert(self):
        u = User.create(name='john', email='john@example.com', password='john')
        email = u.email
        assert email == "john@example.com"

if __name__ == '__main__':
    unittest.main()
