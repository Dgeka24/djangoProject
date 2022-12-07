from django.db import models

class CV(models.Model):
    user = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    skills = models.CharField(max_length=500)
    interests = models.CharField(max_length=500, default='None')
    education = models.CharField(max_length=500, default='None')
    experience = models.CharField(max_length=500, default='None')
    #img = models.ImageField(verbose_name='Imagen', upload_to="images/", null=True, blank=True)
    #img = models.ImageField(upload_to = "images/", blank=True, null=True)

