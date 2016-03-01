from django.contrib import admin

# Register your models here.

from shorten_app.models import Url, Click

admin.site.register(Url)
admin.site.register(Click)
