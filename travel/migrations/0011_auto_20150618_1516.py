# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0010_auto_20150618_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='milestone',
            name='latitude',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='milestone',
            name='longitude',
            field=models.FloatField(blank=True),
        ),
    ]
