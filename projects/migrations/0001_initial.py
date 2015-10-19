# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=60)),
                ('description', models.TextField()),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_started', models.DateTimeField(null=True, blank=True)),
                ('deadline', models.DateTimeField()),
                ('status', models.CharField(max_length=10, choices=[(b'created', b'Created'), (b'published', b'Published'), (b'succeeded', b'Succeeded'), (b'removed', b'Removed'), (b'failed', b'Failed')])),
            ],
        ),
    ]
