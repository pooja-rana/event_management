from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    """ This is user manager for create user  details"""
    def create_user(self, username, password=None, role='User'):
        if not username:
            raise ValueError("Users must have a username")
        user = self.model(username=username, role=role)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None):
        return self.create_user(username, password, role='Admin')

class User(AbstractBaseUser):
    """ user details register model"""
    ROLE_CHOICES = [('Admin', 'Admin'), ('User', 'User')]

    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    #USERNAME_FIELD = 'username'

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        """ username of each user """
        return self.username

class Event(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()
    total_tickets = models.PositiveIntegerField()
    tickets_sold = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    purchase_date = models.DateTimeField(auto_now_add=True)
