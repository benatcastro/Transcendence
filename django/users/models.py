from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .manager import TranscendenceUserManager


class TranscendenceUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=55, unique=True)
    email = models.EmailField("email address", unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='transcendence_user_groups',
        blank=True,
        help_text='The groups this user belongs to.',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='transcendence_user_permissions',
        blank=True,
        help_text='Specific permissions for this user.',
    )
    FT_API = "FT"
    GOOGLE = "GO"
    REGULAR = "RE"
    CREATION_CHOICES = [
        (FT_API, "42_API"),
        (GOOGLE, "Google-Auth"),
        (REGULAR, "Regular")
    ]

    creation_method = models.CharField(
        max_length=2,
        choices=CREATION_CHOICES,
        default=REGULAR
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = TranscendenceUserManager()

    def __str__(self):
        return self.email
