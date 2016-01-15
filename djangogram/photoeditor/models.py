from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models


def get_upload_file_name(instance, filename):
    # filename = instance.user.id + instance.file_extension
    return 'uploads/user_{0}/{1}'.format(instance.user.id, filename)


class Photo(models.Model):
    image = models.ImageField(upload_to=get_upload_file_name)
    name = models.CharField(max_length=100, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)


class UserProfile(models.Model):
    social_id = models.CharField(max_length=100, blank=True)
    user = models.OneToOneField(User)
    profile_pics = models.TextField()
