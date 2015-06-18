# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0003_auto_20150617_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='milestone',
            field=models.ForeignKey(to='travel.Milestone'),
        ),
    ]
