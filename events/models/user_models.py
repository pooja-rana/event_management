from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """ user details register model"""
    ROLE_CHOICES = [('Admin', 'Admin'), ('User', 'User')]

    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        """ username of each user """
        return self.username