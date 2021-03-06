# Generated by Django 3.0.8 on 2020-07-15 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20200611_1820'),
        ('users', '0004_user_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='downvoted_questions',
            field=models.ManyToManyField(related_name='downvoted_users', to='main.Answer'),
        ),
        migrations.AlterField(
            model_name='user',
            name='upvoted_questions',
            field=models.ManyToManyField(related_name='upvoted_users', to='main.Answer'),
        ),
    ]
