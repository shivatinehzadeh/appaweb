# Generated by Django 3.0.5 on 2020-05-31 07:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20200531_1130'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='birth_date',
            new_name='phone',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='location',
        ),
    ]
