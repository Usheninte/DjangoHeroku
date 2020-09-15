from django.db import models
from django.urls import reverse_lazy


class ContactInfo(models.Model):
    email = models.EmailField()
    full_name = models.CharField(max_length=500)
    subject = models.CharField(max_length=150)
    message = models.TextField()

    def __str__(self):
        return "{}".format(self.subject)

    def get_absolute_url(self):
        return reverse_lazy('contact:home')
