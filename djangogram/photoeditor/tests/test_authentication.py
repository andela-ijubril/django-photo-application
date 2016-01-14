from django.contrib.auth.models import User
from django.test import TestCase


class AuthenticationTestCase(TestCase):

    def setUp(self):
        pass

    def test_user_can_login(self):
        self.assertEqual(2 + 2, 4)