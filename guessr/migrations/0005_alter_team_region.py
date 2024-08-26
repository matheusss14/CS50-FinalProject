# Generated by Django 5.0.7 on 2024-08-16 18:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guessr', '0004_region'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='region',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='teams', to='guessr.region'),
        ),
    ]
