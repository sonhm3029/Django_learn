from django.db import models


LANGUAGE_CHOICES = [("python","Python"), ("java","Java"), ("c++","C++")]

# Create your models here.

class Snippet(models.Model):
    code = models.CharField(max_length=50)
    language = models.CharField(choices=LANGUAGE_CHOICES, default=LANGUAGE_CHOICES[0], max_length=50)
    created = models.DateTimeField(auto_now_add=True)
