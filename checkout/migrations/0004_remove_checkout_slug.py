# Generated by Django 5.0.4 on 2024-05-29 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_alter_checkout_image_ids_alter_checkout_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkout',
            name='slug',
        ),
    ]
