# Generated by Django 3.0 on 2019-12-23 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rate', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
