# Generated by Django 3.1.7 on 2021-07-11 10:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20210711_0609'),
    ]

    operations = [
        migrations.AddField(
            model_name='add',
            name='user_file',
            field=models.ImageField(default=None, upload_to=''),
        ),
        migrations.AlterField(
            model_name='add',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 7, 11, 10, 52, 37, 554031)),
        ),
    ]
