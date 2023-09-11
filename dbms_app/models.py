import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework_simplejwt.tokens import RefreshToken


# Create your models here.

class User(AbstractUser):
    """
    Extended User model to create tokens
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    middle_name = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=17, unique=True, blank=True)

    def __str__(self) -> str:
        return self.username
    
    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }


# TODO: Create Student model

# TODO: Create Staff model

# TODO: Create Course model

# TODO: Create ResearchProject model

# TODO: Create AdminResponsibility model

# TODO: Create PerformanceEvaluation model

# TODO: Create Department model

# TODO: Create Faculty model

# TODO: Create University model
