# Generated by Django 3.0.7 on 2021-02-23 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_profile_karma'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='karma',
            field=models.IntegerField(),
        ),
    ]
