# Generated by Django 4.0.1 on 2022-06-17 15:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='predictions',
            name='predicted_on',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
