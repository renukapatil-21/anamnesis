# Generated by Django 3.1.7 on 2021-07-11 14:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_auto_20210711_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 7, 11, 14, 48, 15, 947513)),
        ),
    ]