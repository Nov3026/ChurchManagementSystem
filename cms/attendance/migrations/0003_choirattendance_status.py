# Generated by Django 5.1.3 on 2024-12-07 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='choirattendance',
            name='status',
            field=models.CharField(choices=[('present', 'Present'), ('absent', 'Absent'), ('late', 'Late'), ('excuse', 'Excuse')], default='present', max_length=20),
        ),
    ]
