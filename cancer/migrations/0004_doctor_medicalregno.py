# Generated by Django 4.0.4 on 2022-05-29 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cancer', '0003_doctor'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='medicalregno',
            field=models.CharField(default=0, max_length=15),
        ),
    ]