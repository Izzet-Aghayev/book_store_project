from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    is_employee = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='main_user_groups',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='main_user_permissions',
        blank=True
    )

    def save(self, *args, **kwargs):
        if self.password and not self.password.startswith('pbkdf2_'):
            self.set_password(self.password)  
        super().save(*args, **kwargs)


    def __str__(self):
        return self.email
