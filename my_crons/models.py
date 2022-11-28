from django.db import models

# Create your models here.


class Text(models.Model):
    text = models.CharField(max_length=500)