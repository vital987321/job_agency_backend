# Generated by Django 5.0.3 on 2024-08-31 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agencyapp', '0024_remove_vacancy_company_vacancy_partner'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='seen',
            field=models.BooleanField(default=False),
        ),
    ]
