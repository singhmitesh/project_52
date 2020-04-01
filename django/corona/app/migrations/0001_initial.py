# Generated by Django 2.1.7 on 2020-03-21 11:21

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cases',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('telephone', phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text='Contact phone number', max_length=128, null=True, region=None)),
                ('X', models.FloatField()),
                ('y', models.FloatField()),
                ('condition', models.CharField(max_length=500)),
                ('age', models.IntegerField()),
                ('sex', models.CharField(max_length=50)),
                ('food_need', models.CharField(blank=True, max_length=500, null=True)),
                ('hygine_need', models.CharField(blank=True, max_length=500, null=True)),
                ('other_need', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]