from photoeditor.models import UserProfile


def save_user_profile(backend, user, response, *args, **kwargs):
    """
    Save facebook profile into the UserProfile table
    """
    if backend.name == "facebook":
        img_url = "http://graph.facebook.com/{0}/picture".format(
            response['id'])

    # Query the userprofile database
    profile = UserProfile.objects.get_or_create(user=user)[0]
    profile.profile_pics = img_url
    profile.save()
