# Generated by Django 2.2.7 on 2019-12-25 15:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cpu_util', '0003_auto_20191225_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='record_datetime',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 25, 15, 28, 29, 885960, tzinfo=utc)),
        ),
    ]
