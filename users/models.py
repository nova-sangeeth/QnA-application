from django.db import models
from django.contrib.auth.models import AbstractUser
from main.models import Question, Answer
from django.db.models import Q
from django.contrib.auth.models import User
from functools import reduce


# from django.contrib.auth import get_user_model

# User = get_user_model()


class User(AbstractUser):
    class Meta:
        db_table = "auth_user"

    upvoted_questions = models.ManyToManyField(Question, related_name="upvoted_users")
    downvoted_questions = models.ManyToManyField(
        Question, related_name="downvoted_users"
    )
    upvoted_answers = models.ManyToManyField(Answer, related_name="upvoted_users")
    downvoted_answers = models.ManyToManyField(Answer, related_name="downvoted_users")
    points = models.IntegerField(default=0)
    adjustment_points = models.IntegerField(default=0)
    is_shadow_banned = models.BooleanField(default=False)

    def update_points(self):
        answers = self.answer_set.filter(~Q(points=0))
        points = map(lambda a: a.points, answers)
        user_points = reduce(lambda x, y: x + y, points, 0)
        self.points = user_points + self.adjustment_points
        self.save()


class user_profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    Country = models.CharField(max_length=64, null=True)
    Phone = models.IntegerField(null=True)
    Date_of_Birth = models.DateField(auto_now=False, auto_now_add=False, null=True)

    def __str__(self):
        return self.user

