# Generated by Django 5.0.3 on 2024-03-30 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agencyapp', '0009_vacancy_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='hours_from',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='hours_to',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
