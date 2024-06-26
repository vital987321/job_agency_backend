# Generated by Django 5.0.3 on 2024-04-04 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agencyapp', '0011_application_first_name_application_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='residence_type',
            field=models.IntegerField(blank=True, choices=[(1, 'EU citizenship'), (2, 'Permanent rsidance'), (3, 'Residance permit with free acces to job market'), (4, 'Blue card'), (5, 'Working card'), (6, 'Working visa'), (7, 'No visa')], null=True),
        ),
    ]
