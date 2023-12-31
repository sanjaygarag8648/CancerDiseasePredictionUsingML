# Generated by Django 4.0.4 on 2022-05-29 08:30

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cancer', '0002_patient_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=60, validators=[django.core.validators.RegexValidator('^[a-zA-z][a-zA-Z]+[a-zA-Z]*$', 'Only Alphabets allowed')])),
                ('mobile', models.BigIntegerField(default=0, validators=[django.core.validators.RegexValidator('^[5-9][0-9]{9}$', 'Enter 10 digits mobile number')])),
                ('photo', models.ImageField(upload_to='doctor_photos')),
                ('specialization', models.CharField(choices=[('gastroenterologist', 'gastroenterologist'), ('Hematologist-oncologist', 'Hematologist-oncologist'), ('Thoracic-oncologists', 'Thoracic-oncologists')], max_length=60)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=12)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='doctor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
