from django.db import models

# Create your models here.

class Url(models.Model):
    url = models.URLField()
    title = models.CharField(max_length=100)
    description = models.TextField()
    short_version = models.CharField(max_length=30)
    added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.url

    class Meta:
        ordering = ["-added"]



class Clicks(models.Model):
    time_of_click = models.DateTimeField(auto_now_add=True)
    referenced_url = models.ForeignKey(Url)

    def __str__(self):
        return self.time_of_click

    class Meta:
        ordering = ["-time_of_click"]