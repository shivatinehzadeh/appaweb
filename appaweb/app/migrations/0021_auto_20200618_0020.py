# Generated by Django 3.0.5 on 2020-06-17 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_auto_20200613_1732'),
    ]

    operations = [
        migrations.AddField(
            model_name='sell',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AddField(
            model_name='sellonline',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]