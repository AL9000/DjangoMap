# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0004_segment_end_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('user', models.CharField(max_length='25')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('segment', models.ForeignKey(to='travel.Segment')),
            ],
        ),
    ]
