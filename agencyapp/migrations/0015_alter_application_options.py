# Generated by Django 5.0.3 on 2024-07-12 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agencyapp', '0014_vacancy_active_alter_application_status_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='application',
            options={'ordering': ['-created_at']},
        ),
    ]
