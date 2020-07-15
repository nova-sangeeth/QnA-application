from django.db import models
from django.contrib.auth.models import AbstractUser
from main.models import Question

from django.contrib.auth.models import User

# from django.contrib.auth import get_user_model

# User = get_user_model()


class User(AbstractUser):
    class Meta:
        db_table = "auth_user"

    upvoted_questions = models.ManyToManyField(Question, related_name="upvoted_users")
    downvoted_questions = models.ManyToManyField(
        Question, related_name="downvoted_users"
    )


class user_profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    Country = models.CharField(max_length=64, null=True)
    Phone = models.IntegerField(null=True)

    def __str__(self):
        return self.user

