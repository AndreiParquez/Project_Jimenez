# Generated by Django 5.0.1 on 2025-01-26 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0004_roomimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='guest',
            field=models.CharField(max_length=100),
        ),
    ]
