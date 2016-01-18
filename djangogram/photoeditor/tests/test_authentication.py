from django.contrib.auth.models import User
from django.test import TestCase, Client


class AuthenticationTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='awesome', password='tested')

    def test_user_can_login(self):
        pass

    def test_authenticated_routes(self):
        pass
