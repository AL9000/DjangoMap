# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0014_auto_20150620_0019'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='photo',
            field=models.ImageField(null=True, upload_to='photos/comments/'),
        ),
        migrations.AlterField(
            model_name='milestone',
            name='arrival_date',
            field=models.DateTimeField(verbose_name="date d'arrivée"),
        ),
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(upload_to='photos/milestone/'),
        ),
    ]
