# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0017_photo_legend'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='legend',
            field=models.TextField(verbose_name='legend', blank=True),
        ),
    ]
