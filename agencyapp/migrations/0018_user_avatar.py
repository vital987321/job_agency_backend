# Generated by Django 5.0.3 on 2024-07-17 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agencyapp', '0017_remove_user_favourite_user_favourites'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='media\x07vatars'),
        ),
    ]