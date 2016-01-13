from django.http import HttpResponse, JsonResponse
from django.shortcuts import render_to_response, redirect, render
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView, View
from forms import PhotoForm
from models import Photo
from djangogram.settings.base import MAX_IMAGE_SIZE
import json

# from django.template.context import RequestContext


class IndexView(TemplateView):
    template_name = 'photoeditor/canvas.html'


class LoginRequiredMixin(object):
    """
    Enforce login on some views
    """

    @method_decorator(login_required(login_url='/'))
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(
            request, *args, **kwargs)


def login(request):
    # context = RequestContext(request, {
    #     'request': request, 'user': request.user})
    # return render_to_response('login.html', context_instance=context)
    return render(request, 'photoeditor/login.html')


@login_required(login_url='/')
def home(request):
    return render_to_response('photoeditor/canvas.html')


def logout(request):
    auth_logout(request)
    return redirect('/')


class HomeView(TemplateView):
    template_name = 'photoeditor/canvas.html'
    form_class = PhotoForm

    def post(self, request, *args, **kwargs):

        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            file_size = form.files['image'].size
            if file_size <= MAX_IMAGE_SIZE:
                form.save()
                return JsonResponse({
                    'status': 'success'
                }, status=200)
        return JsonResponse({
                    'status': 'failed'
                }, status=403)

    def get_context_data(self, **kwargs):
        # get all images belonging to logged in user
        images = Photo.objects.all()


        context = super(HomeView, self).get_context_data(**kwargs)

        context['images'] = images
        return context
