# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0004_auto_20150617_1904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='milestone',
            field=models.ForeignKey(to='travel.Milestone', related_name='comments'),
        ),
    ]
