# Generated by Django 2.1.7 on 2020-03-22 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20200322_0937'),
    ]

    operations = [
        migrations.AddField(
            model_name='cases',
            name='address',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
