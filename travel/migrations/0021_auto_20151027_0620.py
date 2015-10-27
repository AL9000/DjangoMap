# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0020_milestone_draft'),
    ]

    operations = [
        migrations.AlterField(
            model_name='milestone',
            name='draft',
            field=models.BooleanField(help_text='Only admins can see and modify drafts.', verbose_name='Is it a draft ?', default=False),
        ),
    ]
