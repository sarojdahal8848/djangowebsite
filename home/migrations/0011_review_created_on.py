# Generated by Django 3.0 on 2019-12-24 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_review_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='created_on',
            field=models.DateField(auto_now=True),
        ),
    ]