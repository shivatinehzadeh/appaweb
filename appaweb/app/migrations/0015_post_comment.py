# Generated by Django 3.0.5 on 2020-06-05 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_profile_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
    ]
