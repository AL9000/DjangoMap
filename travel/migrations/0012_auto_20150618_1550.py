# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0011_auto_20150618_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='milestone',
            name='latitude',
            field=models.FloatField(help_text='Latitude and longitude fields will be filled up automatically from city name above', blank=True),
        ),
    ]
