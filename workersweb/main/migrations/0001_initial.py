# Generated by Django 5.0.6 on 2024-06-25 13:20

import django.db.models.deletion
import main.models
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('username', models.CharField(blank=True, max_length=255, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_worker', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', main.models.CustomUserManager()),
            ],
        ),
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_no', models.CharField(max_length=15)),
                ('adrress', models.TextField()),
                ('district', models.CharField(max_length=255)),
                ('pin', models.CharField(max_length=6)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('avatar', models.ImageField(upload_to='uploads/avatars')),
                ('district', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('street_address', models.TextField()),
                ('pin', models.CharField(max_length=6)),
                ('phone_no', models.CharField(max_length=15)),
                ('experience', models.IntegerField()),
                ('job_title', models.CharField(max_length=255)),
                ('resume', models.FileField(upload_to='uploads/resume')),
                ('notification', models.BooleanField(default=False)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('desc', models.TextField()),
                ('status', models.BooleanField(default=False)),
                ('work_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.worker')),
            ],
        ),
    ]
