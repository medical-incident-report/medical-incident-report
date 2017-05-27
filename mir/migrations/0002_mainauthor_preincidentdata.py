# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import opal.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('opal', '0028_auto_20170210_1146'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mir', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainAuthor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('updated', models.DateTimeField(null=True, blank=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('surname', models.CharField(max_length=255, blank=True)),
                ('first_name', models.CharField(max_length=255, blank=True)),
                ('middle_name', models.CharField(max_length=255, null=True, blank=True)),
                ('email', models.CharField(max_length=255, null=True, blank=True)),
                ('role', models.TextField(null=True, blank=True)),
                ('title_ft', models.CharField(default=b'', max_length=255, null=True, blank=True)),
                ('birth_place_ft', models.CharField(default=b'', max_length=255, null=True, blank=True)),
                ('birth_place_fk', models.ForeignKey(blank=True, to='opal.Destination', null=True)),
                ('created_by', models.ForeignKey(related_name='created_mir_mainauthor_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('patient', models.ForeignKey(to='opal.Patient')),
                ('title_fk', models.ForeignKey(blank=True, to='opal.Title', null=True)),
                ('updated_by', models.ForeignKey(related_name='updated_mir_mainauthor_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
        migrations.CreateModel(
            name='PreIncidentData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('updated', models.DateTimeField(null=True, blank=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('created_by', models.ForeignKey(related_name='created_mir_preincidentdata_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('patient', models.ForeignKey(to='opal.Patient')),
                ('updated_by', models.ForeignKey(related_name='updated_mir_preincidentdata_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
    ]
