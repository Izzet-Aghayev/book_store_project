from django.db import models
from django.contrib.auth.models import AbstractUser
from accounts.managers import UserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
    MinLengthValidator,
)


from .managers import UserManager


class User(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)
    is_employee = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email



class Profile(models.Model):
    user = models.OneToOneField(User, models.CASCADE)

    email = models.EmailField(editable=False)
    about = models.TextField(null=True, blank=True)
    account_balance =  models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)], null=True, blank=True)
    profile_image = models.ImageField(upload_to='profile', null=True, blank=True)

    def __str__(self):
        return self.email