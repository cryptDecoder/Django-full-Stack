from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    pass


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    pass


class Lead(models.Model):
    SOURCE_CHOICES = (
        ("YouTube", "YouTube"),
        ("Google", "Google"),
        ("NewsLetter", "NewsLetter"),
    )

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)
    pass
