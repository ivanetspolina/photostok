# Generated by Django 5.0.6 on 2024-06-02 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_category_options_remove_category_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='default-slug', unique=True),
        ),
    ]
