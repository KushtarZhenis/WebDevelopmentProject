# Generated by Django 5.0.4 on 2024-04-18 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='description',
        ),
        migrations.AddField(
            model_name='author',
            name='bookCount',
            field=models.IntegerField(default=0),
        ),
    ]