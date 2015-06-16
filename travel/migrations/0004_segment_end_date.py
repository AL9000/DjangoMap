# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0003_auto_20150616_1324'),
    ]

    operations = [
        migrations.AddField(
            model_name='segment',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 6, 16, 11, 28, 22, 545132, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
