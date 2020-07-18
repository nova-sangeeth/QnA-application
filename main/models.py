from django.db import models, models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone
from .helpers import x_ago_helper

# from django.utils.datetime_safe import time

# Create your models here.


class Question(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True)
    body = models.TextField(blank=True, null=True)
    created = models.DateTimeField(editable=False, null=True)
    modified = models.DateTimeField(null=True)
    answers_count = models.IntegerField(default=0, null=True)
    points = models.IntegerField(default=0, null=True)
    hidden = models.BooleanField(default=False)

    @property
    def num_answers(self):
        answers = Answer.objects.filter(question_id=self.id)
        return len(answers)

    def x_ago(self):
        diff = timezone.now() - self.created
        return x_ago_helper(diff)

    # showing points to the user
    def show_points(self):
        if self.points < 0:
            return 0
        else:
            return self.points

    def update_points(self):
        upvotes = self.upvoted_users.distinct().count()
        downvotes = self.downvoted_users.distinct().count()
        downvotes += self.downvoted_users.filter(is_staff=True).count() * 2
        self.points = upvotes - downvotes
        self.save()

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Question, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    created = models.DateTimeField(editable=False, null=True)
    modified = models.DateTimeField(null=True)
    points = models.IntegerField(default=0, null=True)
    hidden = models.BooleanField(default=False)
    # writing a method to show how long ago the post was put up.
    @property
    def x_ago(self):
        diff = timezone.now() - self.created
        return x_ago_helper(diff)

    def show_points(self):
        if self.points < 0:
            return 0
        else:
            return self.points

    def update_points(self):
        upvotes = self.upvoted_users.distinct().count()
        downvotes = self.downvoted_users.distinct().count()
        downvotes += self.downvoted_users.filter(is_staff=True).count() * 2
        self.points = upvotes - downvotes
        self.save()

    def save(self, *args, **kwargs):
        """ On save, update timestamps """
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Answer, self).save(*args, **kwargs)

    def __str__(self):
        return self.text
