# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0015_auto_20150712_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='photo',
            field=models.ImageField(blank=True, default=1, upload_to='photos/comments/'),
            preserve_default=False,
        ),
    ]
