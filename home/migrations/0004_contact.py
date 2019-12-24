# Generated by Django 3.0 on 2019-12-22 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_saying_fullname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=250, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('message', models.TextField(null=True)),
                ('subject', models.CharField(max_length=250, null=True)),
            ],
        ),
    ]
