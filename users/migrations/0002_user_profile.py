# Generated by Django 3.0.8 on 2020-07-15 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Country', models.CharField(max_length=64, null=True)),
                ('Phone', models.IntegerField(max_length=15, null=True)),
            ],
        ),
    ]
