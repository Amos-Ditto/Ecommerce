from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .manager import AppUserManager


class AppUser(AbstractBaseUser):
    email = models.EmailField(verbose_name="email address", max_length=255, unique=True)
    full_name = models.CharField(verbose_name="full name", max_length=255)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = AppUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "full_name",
    ]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin