from django.http import HttpResponseRedirect
from django.shortcuts import render
from hashids import Hashids
# Create your views here.
from django.views.generic import View, CreateView, ListView
from django.core.urlresolvers import reverse
from shorten_app.forms import UrlForm
from shorten_app.models import Url, Clicks


class IndexView(View):
    def get(self, request):
        url_form = UrlForm()
        last_url = Url.objects.first()
        return render(request, 'index.html', {"form": url_form, 'last_url': last_url})

    def post(self, request):
        hashids = Hashids(min_length=5)
        form_instance = UrlForm(request.POST)
        if form_instance.is_valid():
            url_object = form_instance.save()
            hashid = hashids.encode(url_object.id)

            url_object.short_version = hashid
            url_object.save()

        return HttpResponseRedirect(reverse("index"))


class AllClick(ListView):
    model = Clicks


class AllLink(ListView):
    model = Url




def redirect(request, captured_id):
    redirect_url_object = Url.objects.get(short_version=captured_id)
    redirect_url = redirect_url_object.url

    Clicks.objects.create(referenced_url=redirect_url_object)

    return HttpResponseRedirect(redirect_url)
