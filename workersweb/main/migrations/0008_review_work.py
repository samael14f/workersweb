# Generated by Django 5.0.6 on 2024-07-03 20:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_work_is_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='work',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.work'),
            preserve_default=False,
        ),
    ]
