# Generated by Django 4.1.5 on 2023-01-29 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0010_alter_place_description_long'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='slug',
        ),
    ]
