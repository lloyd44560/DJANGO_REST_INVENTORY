from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Product(models.Model):

    name =  models.CharField(max_length = 180)
    date_created = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)

    def __str__(self):
        return self.name