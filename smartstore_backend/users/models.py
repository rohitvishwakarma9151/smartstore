from django.db import models
from django.contrib.auth.models import AbstractUser

# Create Admin models here.

class User(AbstractUser):
    is_Admin = models.BooleanField(default=False)


    def __str__(self):
        return self.username