# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0019_auto_20151020_0817'),
    ]

    operations = [
        migrations.AddField(
            model_name='milestone',
            name='draft',
            field=models.BooleanField(default=False),
        ),
    ]
