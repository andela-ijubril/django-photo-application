from __future__ import unicode_literals

import os
from time import time
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver


def get_upload_file_name(instance, filename):
    # filename = instance.user.id + instance.file_extension
    return 'uploads/user_{0}/{1}_{2}'.format(instance.user.id, str(time()).replace('.', ''), filename)


class Photo(models.Model):
    image = models.ImageField(upload_to=get_upload_file_name)
    name = models.CharField(max_length=100, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)

    class Meta:
        ordering = ['-created']


class UserProfile(models.Model):
    social_id = models.CharField(max_length=100, blank=True)
    user = models.OneToOneField(User)
    profile_pics = models.TextField()


@receiver(post_delete, sender=Photo)
def delete_image(sender, instance, **kwargs):

    image_path = instance.image.path

    if os.path.exists(image_path):
        os.remove(image_path)
