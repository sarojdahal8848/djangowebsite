# Generated by Django 3.0 on 2019-12-24 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20191224_1223'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
