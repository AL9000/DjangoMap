# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0016_auto_20150804_2355'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='legend',
            field=models.TextField(verbose_name='legend', default=''),
            preserve_default=False,
        ),
    ]
