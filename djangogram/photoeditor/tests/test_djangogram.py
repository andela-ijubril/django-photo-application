from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from photoeditor.models import UserProfile


class DjangogramTest(TestCase):

    def setUp(self):
        self.client = Client()

        self.user = User.objects.create_user(username='itest', password='awesome')
        self.user.save()
        self.profile = UserProfile.objects.get_or_create(user=self.user)[0]
        self.profile.photo = "https://urltoimage/theimage.jpg"
        self.profile.save()
        self.login = self.client.login(username='itest', password='awesome')

    def test_user_can_reach_index_page(self):
        url = reverse("index")
        # import pdb; pdb.set_trace()
        response = Client().get(url)
        self.assertEqual(response.status_code, 200)

    def test_authenticated_routes(self):
        url = reverse("home")
        response = Client().get(url)
        self.assertEqual(response.status_code, 302)

    def test_can_reach_home_page(self):
        self.login = self.client.login(username='itest', password='awesome')
        url = reverse("home")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
