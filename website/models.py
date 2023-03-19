from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Club(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    created_at =  models.DateTimeField(auto_now_add=True)
    students = ArrayField(models.IntegerField(), null=True)

    def __str__(self):
        return self.name