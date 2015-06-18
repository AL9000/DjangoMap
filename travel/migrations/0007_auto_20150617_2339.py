# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0006_auto_20150617_1952'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='milestone',
            name='pub_date',
        ),
        migrations.AlterField(
            model_name='milestone',
            name='arrival_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
