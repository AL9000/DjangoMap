# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0002_auto_20150615_1809'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='segment',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='segment',
            name='start_date',
        ),
        migrations.AddField(
            model_name='segment',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 6, 16, 11, 24, 31, 502449, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
