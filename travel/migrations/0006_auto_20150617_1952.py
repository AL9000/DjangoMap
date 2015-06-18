# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0005_auto_20150617_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='milestone',
            name='text',
            field=django_markdown.models.MarkdownField(),
        ),
    ]
