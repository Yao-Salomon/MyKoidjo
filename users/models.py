from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    matricule = models.CharField(max_length=20, unique=True, verbose_name="Matricule")
    age = models.PositiveIntegerField(null=True, blank=True, verbose_name="Âge")

    def __str__(self):
        return f"{self.username} ({self.matricule})"
# Create your models here.
