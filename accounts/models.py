from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    age=models.CharField(max_length=3,null=True,blank=True)