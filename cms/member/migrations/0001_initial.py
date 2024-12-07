# Generated by Django 5.1.3 on 2024-12-06 13:54

import django.core.validators
import django.db.models.deletion
import django_countries.fields
import validator.views
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=150)),
                ('middle_name', models.CharField(blank=True, max_length=150, null=True)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('gender', models.CharField(choices=[('female', 'Female'), ('male', 'Male')], max_length=10)),
                ('dob', models.DateField(blank=True, null=True, verbose_name='date of birth')),
                ('nationality', django_countries.fields.CountryField(blank='selected country', max_length=2)),
                ('phone1', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+233000000000'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')], verbose_name='Prim. Phone')),
                ('phone2', models.CharField(blank=True, max_length=15, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+233000000000'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')], verbose_name='Sec. Phone')),
                ('address', models.TextField(max_length=250)),
                ('photo_url', models.FileField(blank=True, max_length=256, null=True, upload_to='members', validators=[validator.views.validate_file_size], verbose_name='profile photo')),
                ('status', models.CharField(choices=[('active', 'Active'), ('non_active', 'Non Active'), ('suspended', 'Suspended'), ('deceased', 'Deceased')], default='active', max_length=25)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='member_created', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='member_user', to=settings.AUTH_USER_MODEL, verbose_name='username')),
            ],
        ),
    ]