# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0013_auto_20150619_0530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='milestone',
            name='arrival_date',
            field=models.DateField(verbose_name="date d'arrivée"),
        ),
    ]
