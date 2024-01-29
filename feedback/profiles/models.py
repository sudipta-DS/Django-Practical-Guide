from django.db import models

# Create your models here.

class ProfilesModel(models.Model):
    image = models.FileField(upload_to='images')