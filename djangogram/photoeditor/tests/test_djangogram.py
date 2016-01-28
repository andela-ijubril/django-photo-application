import os
from io import BytesIO
import mock

from PIL import Image

from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, Client, RequestFactory
from django.core.urlresolvers import reverse
from django.core.files import File

from photoeditor.models import UserProfile, Photo
from photoeditor.views import HomeView, EffectView, DeleteView
from photoeditor.forms import PhotoForm


def create_dummy_image():
    file = BytesIO()
    image = Image.new('RGBA', size=(50, 50), color=(155, 0, 0))
    image.save(file, 'png')
    file.name = 'test_image.png'
    file.seek(0)
    return file


class DjangogramTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.factory = RequestFactory()

        self.user = User.objects.create_user(username='itest', password='awesome')
        self.user.save()
        self.profile = UserProfile.objects.get_or_create(user=self.user)[0]
        self.profile.photo = "https://urltoimage/theimage.jpg"
        self.profile.save()

        self.file_mock = mock.MagicMock(spec=File)
        self.file_mock.name = "myimage.jpg"
        self.client.login(username='itest', password='awesome')
        self.file = create_dummy_image()

        self.photo = Photo.objects.create(image=self.file.name, user=self.user)

    def test_user_can_reach_index_page(self):
        url = reverse("index")
        response = Client().get(url)
        self.assertEqual(response.status_code, 200)

    def test_authenticated_routes(self):
        url = reverse("home")
        response = Client().get(url)
        self.assertEqual(response.status_code, 302)

    def test_can_reach_home_page(self):
        url = reverse("home")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_file_was_uploaded(self):

        # test File  Uploaded
        image = SimpleUploadedFile(self.file.name,
                                   self.file.read(),
                                   content_type="image")
        request = self.factory.post(
            '/home',
            {
             'image': image},
            enctype="multipart/form-data")
        request.user = self.user
        response = HomeView.as_view()(request)
        self.assertEquals(response.status_code, 200)

    @mock.patch('photoeditor.models.Photo.objects.get')
    @mock.patch.object(Image, 'open')
    @mock.patch('ntpath.basename', return_value='open')
    def test_effect_was_applied(self, mock_file, mock_image, mock_path):
        request = self.factory.post(
            '/effect/', {
                    'image_id': self.photo.id,
                    'effect_name': 'blur'
                }
        )
        request.user = self.user
        response = EffectView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    @mock.patch("photoeditor.models.Photo.objects.get")
    @mock.patch("os.path.exists", return_value=True)
    @mock.patch("os.remove")
    def test_can_delete_image(self, mock_get, mock_path, mock_remove):
        request = self.factory.post(
            '/delete/', {
                'path': self.photo.image.path,
                    'imageId': 1
                }
        )
        request.user = self.user

        response = DeleteView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(Photo.objects.get)
        self.assertTrue(os.remove)
