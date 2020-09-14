from django.db import models


class ContactInfo(models.Model):
    email = models.EmailField()
    full_name = models.CharField(max_length=500)
    subject = models.CharField(max_length=150)
    message = models.TextField()
