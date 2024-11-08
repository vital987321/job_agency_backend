# Generated by Django 5.0.3 on 2024-06-28 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agencyapp', '0013_alter_user_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='application',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending', max_length=50),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='residence_type',
            field=models.IntegerField(blank=True, choices=[(1, 'EU citizenship'), (2, 'Permanent residence'), (3, 'Residance permit with free access to job market'), (4, 'Blue card'), (5, 'Working card'), (6, 'Working visa'), (7, 'No visa')], null=True),
        ),
    ]
