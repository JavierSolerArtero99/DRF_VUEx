# Generated by Django 3.0.7 on 2021-02-23 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='karma',
            field=models.IntegerField(default=0),
        ),
    ]
