# Generated by Django 5.0.7 on 2024-08-16 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guessr', '0002_userstats_g1g_userstats_g2g_userstats_g3g_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='image',
            field=models.TextField(null=True),
        ),
    ]
