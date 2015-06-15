# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='segment',
            name='photo',
            field=models.ImageField(upload_to='photos/', default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='segment',
            name='text',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='segment',
            name='slug',
            field=models.SlugField(unique=True, max_length=100, blank=True),
        ),
    ]
