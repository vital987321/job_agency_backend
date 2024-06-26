# Generated by Django 5.0.3 on 2024-03-25 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agencyapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Field',
            new_name='Sector',
        ),
        migrations.RemoveField(
            model_name='vacancy',
            name='field',
        ),
        migrations.AddField(
            model_name='vacancy',
            name='sector',
            field=models.ManyToManyField(blank=True, related_name='vacancies', to='agencyapp.sector'),
        ),
    ]
