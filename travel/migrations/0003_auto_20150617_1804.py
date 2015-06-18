# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0002_auto_20150617_1750'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='milestone',
            name='photos',
        ),
        migrations.AddField(
            model_name='photo',
            name='milestone',
            field=models.ForeignKey(default=1, to='travel.Milestone', related_name='photos'),
            preserve_default=False,
        ),
    ]
