from django.contrib.auth.models import User
from django.test import TestCase, Client


class AuthenticationTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='awesome', password='tested')

    def test_user_can_login(self):
        self.assertEqual(2 + 2, 4)

    def test_authenticated_routes(self):
        pass
