# Generated by Django 3.1.7 on 2021-07-11 06:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 7, 11, 6, 9, 15, 66701)),
        ),
    ]
