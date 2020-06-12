# Generated by Django 3.0.6 on 2020-06-05 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created', models.DateTimeField(editable=False)),
                ('modified', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, null=True)),
                ('body', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField()),
                ('answers_count', models.IntegerField(default=0)),
                ('points', models.IntegerField(default=0)),
            ],
        ),
    ]