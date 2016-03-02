from django.http import HttpResponseRedirect
from django.shortcuts import render
from hashids import Hashids
# Create your views here.
from django.views.generic import View, CreateView, ListView, UpdateView
from django.core.urlresolvers import reverse
from shorten_app.forms import UrlForm
from shorten_app.models import Url, Clicks


class IndexView(View):
    def get(self, request):
        last_url = Url.objects.first()
        user_urls = Url.objects.filter(user=self.request.user)

        return render(request, 'index.html', {'last_url': last_url, 'user_urls': user_urls})


class AllClick(ListView):
    model = Clicks


class AllLink(ListView):
    model = Url


class CreateLink(CreateView):
    model = Url
    fields = ('url', 'title', 'description')

    def form_valid(self, form):
        url_object = form.save(commit=False)
        url_object.user = self.request.user
        url_object.save()
        print(url_object.id)
        hashids = Hashids(min_length=5)
        hashid = hashids.encode(url_object.id)
        url_object.short_version = hashid
        url_object.save()
        print(url_object.short_version)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('index')


class EditLink(UpdateView):
    model = Url
    fields = ('url', 'title', 'description')


def redirect(request, captured_id):
    redirect_url_object = Url.objects.get(short_version=captured_id)
    redirect_url = redirect_url_object.url

    Clicks.objects.create(referenced_url=redirect_url_object)

    return HttpResponseRedirect(redirect_url)
