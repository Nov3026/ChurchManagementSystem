# Generated by Django 5.1.3 on 2024-12-07 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('announcement', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='announcement',
            old_name='content',
            new_name='message',
        ),
    ]
