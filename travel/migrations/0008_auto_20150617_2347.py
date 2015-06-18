# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0007_auto_20150617_2339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='milestone',
            name='arrival_date',
            field=models.DateTimeField(),
        ),
    ]
