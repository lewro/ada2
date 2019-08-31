from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):

  user             = models.OneToOneField(User, on_delete=models.CASCADE)
  paid             = models.BooleanField(default=False)
  time_spent       = models.IntegerField(default=0)
