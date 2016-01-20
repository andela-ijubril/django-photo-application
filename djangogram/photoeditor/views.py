import os

from django.core.urlresolvers import reverse
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render_to_response, redirect, render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.template.context_processors import csrf
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, View
from forms import PhotoForm
from models import Photo, UserProfile
from effects import photo_effects, GramEffects
from djangogram.settings.base import MAX_IMAGE_SIZE, UPLOAD_FOLDER
import json
import ntpath


class LoginRequiredMixin(object):
    """
    Enforces User authentication on a view
    """
    @method_decorator(login_required(login_url='/'))
    def dispatch(self, request, *args, **kwargs):
        """
        Override the default dispatch method in a view
        """
        return super(LoginRequiredMixin, self).dispatch(
            request, *args, **kwargs)


class IndexView(TemplateView):
    """
    The Index View for djangogram
    """
    template_name = 'photoeditor/login.html'

    def get(self, request, *args, **kwargs):
        """
        Responds to the get request
        """
        if request.user.is_authenticated():
            return redirect(reverse('home'))

        return render(self.request, self.template_name)


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'photoeditor/canvas.html'
    form_class = PhotoForm

    def post(self, request, *args, **kwargs):

        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
            file_size = form.files['image'].size
            if file_size <= MAX_IMAGE_SIZE:
                photo = form.save(commit=False)
                photo.user = self.request.user
                photo.save()
                return JsonResponse({
                    'status': 'success'
                }, status=200)
        return JsonResponse({
                    'status': 'failed'
                }, status=403)

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['images'] = Photo.objects.filter(user=self.request.user)
        context['profile'] = UserProfile.objects.get(user_id=self.request.user.id)
        return context


class EffectView(View):
    """
    The view that handles the effect to be applied to the image
    """
    def post(self, request, *args, **kwargs):
        """
        Post request that handles effect name and image_id the returns the photo path of the applied image
        """
        effect_name = request.POST['effect_name']
        imageid = request.POST['image_id']

        image_to_filter = Photo.objects.get(id=imageid).image.path
        if effect_name == 'reset':
            new_photo_path = os.path.join(UPLOAD_FOLDER + str(self.request.user.id), ntpath.basename(image_to_filter))
        else:
            applied_effect = GramEffects.g_open(image_to_filter).g_apply(effect_name)
            filename, file_extension = os.path.splitext(image_to_filter)
            photo_path = filename + 'edited' + file_extension
            new_photo_path = os.path.join(UPLOAD_FOLDER + str(self.request.user.id), ntpath.basename(photo_path))

            applied_effect.save(photo_path)

        return JsonResponse({
                    'status': 'success',
                    'applied_effect': new_photo_path
                }, status=200)


class DeleteView(View):
    """
    The view that handles the deleting of image
    """
    def post(self, request, *args, **kwargs):
        image_id = request.POST['image_id']
        photo = Photo.objects.get(id=image_id)
        photo.delete()

        return JsonResponse({
                    'status': 'deleted',
                }, status=200)
