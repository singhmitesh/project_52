# Generated by Django 2.1.7 on 2020-03-22 09:37

from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0002_cases_geom'),
    ]

    operations = [
        migrations.CreateModel(
            name='volunteers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text='Mobile phone number', max_length=128, null=True, region=None)),
                ('landline', models.CharField(blank=True, max_length=500, null=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('servicescanprovide', models.CharField(max_length=5000)),
                ('geom', django.contrib.gis.db.models.fields.GeometryField(blank=True, null=True, srid=4326)),
                ('x', models.FloatField()),
                ('y', models.FloatField()),
                ('country', models.CharField(max_length=5000)),
                ('address', models.CharField(max_length=5000)),
                ('postal_code', models.IntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RenameField(
            model_name='cases',
            old_name='X',
            new_name='x',
        ),
    ]