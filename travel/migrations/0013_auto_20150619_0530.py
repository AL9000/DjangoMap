# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0012_auto_20150618_1550'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'commentaire', 'verbose_name_plural': 'commentaires'},
        ),
        migrations.AlterModelOptions(
            name='milestone',
            options={'verbose_name': 'étape', 'verbose_name_plural': 'étapes'},
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='user',
            new_name='alias',
        ),
        migrations.RemoveField(
            model_name='milestone',
            name='name',
        ),
        migrations.AddField(
            model_name='milestone',
            name='title',
            field=models.CharField(max_length=100, verbose_name='titre', default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='milestone',
            name='video',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(verbose_name='contenu'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='milestone',
            field=models.ForeignKey(verbose_name='étapes', to='travel.Milestone', related_name='comments'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='pub_date',
            field=models.DateTimeField(verbose_name='date de publication', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='milestone',
            name='arrival_date',
            field=models.DateTimeField(verbose_name="date d'arrivée"),
        ),
        migrations.AlterField(
            model_name='milestone',
            name='latitude',
            field=models.FloatField(editable=False),
        ),
        migrations.AlterField(
            model_name='milestone',
            name='longitude',
            field=models.FloatField(editable=False),
        ),
        migrations.AlterField(
            model_name='milestone',
            name='slug',
            field=models.SlugField(max_length=100, editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='milestone',
            name='text',
            field=django_markdown.models.MarkdownField(verbose_name='texte'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='milestone',
            field=models.ForeignKey(verbose_name='étapes', to='travel.Milestone', related_name='photos'),
        ),
    ]
