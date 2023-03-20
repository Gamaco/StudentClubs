from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Club(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    image = models.CharField(max_length=200, default="website\static\sc_nophoto.webp")
    created_at =  models.DateTimeField(auto_now_add=True)
    students = ArrayField(models.IntegerField(), null=True)
    school = models.CharField(max_length=50, default="undefined")
    country = models.CharField(max_length=50, default="undefined")
    category = models.CharField(max_length=50, default="undefined")

    def __str__(self):
        return self.name