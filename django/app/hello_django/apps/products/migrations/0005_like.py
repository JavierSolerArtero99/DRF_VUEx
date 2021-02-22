# Generated by Django 3.0.7 on 2021-02-22 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('products', '0004_product_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('likes', models.IntegerField(default=0)),
                ('likeAuthor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likeAuthor', to='profiles.Profile')),
            ],
        ),
    ]
