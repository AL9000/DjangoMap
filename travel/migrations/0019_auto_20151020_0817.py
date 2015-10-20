# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0018_auto_20151011_0454'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('video', models.URLField(blank=True)),
                ('legend', models.TextField(blank=True, verbose_name='legend')),
            ],
        ),
        migrations.RemoveField(
            model_name='milestone',
            name='video',
        ),
        migrations.AddField(
            model_name='video',
            name='milestone',
            field=models.ForeignKey(to='travel.Milestone', verbose_name='étapes', related_name='videos'),
        ),
    ]
