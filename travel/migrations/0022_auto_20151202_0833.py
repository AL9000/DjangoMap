# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0021_auto_20151027_0620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='milestone',
            name='draft',
            field=models.BooleanField(default=False, help_text='Les brouillons ne seront pas publiés.', verbose_name='Brouillon ?'),
        ),
    ]
