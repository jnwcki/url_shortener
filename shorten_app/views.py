from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views.generic import View
from django.core.urlresolvers import reverse
from shorten_app.forms import UrlForm


class IndexView(View):
    def get(self, request):
        url_form = UrlForm()
        return render(request, 'index.html', {"form": url_form})

    def post(self, request):
        form_instance = UrlForm(request.Post)
        return HttpResponseRedirect(reverse("IndexView"))

class AllClick(IndexView):
    pass

class UserClick(View):
    pass