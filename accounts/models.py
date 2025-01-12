from django.db import models
from django.contrib.auth.models import AbstractUser


class NewUser(AbstractUser):
    email = models.EmailField(unique=True)
    is_employee = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='new_user_groups',  # Yeni əlaqə adı
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='new_user_permissions',  # Yeni əlaqə adı
        blank=True
    )

    def save(self, *args, **kwargs):
        # Şifrə düz mətndirsə, heşləyin
        if self.pk is None and self.password:
            self.set_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email
