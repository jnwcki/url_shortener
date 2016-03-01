from django import forms
from shorten_app.models import Url


class UrlForm(forms.ModelForm):

    class Meta:
        model = Url
        exclude = ['short_version']