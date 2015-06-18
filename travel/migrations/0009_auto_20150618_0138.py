# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0008_auto_20150617_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='milestone',
            name='latitude',
            field=models.FloatField(editable=False),
        ),
        migrations.AlterField(
            model_name='milestone',
            name='longitude',
            field=models.FloatField(editable=False),
        ),
    ]
