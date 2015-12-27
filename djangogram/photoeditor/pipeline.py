from photoeditor.models import UserProfile


def save_user_profile(backend, user, response, *args, **kwargs):
    # Save Facebook profile photo into the user profile
    if backend.name == "facebook":
        img_url = "http://graph.facebook.com/{0}/picture".format(
            response['id'])

    # Query the userprofile database
    profile = UserProfile.objects.get_or_create(user=user)[0]
    profile.photo = img_url
    profile.save()
