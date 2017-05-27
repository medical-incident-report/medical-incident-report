# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import opal.models


class Migration(migrations.Migration):

    dependencies = [
        ('opal', '0028_auto_20170210_1146'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mir', '0004_auto_20170527_1100'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegisterIncident',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('updated', models.DateTimeField(null=True, blank=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('incident_name', models.CharField(max_length=255, blank=True)),
                ('link_to_the_newsfeed', models.CharField(max_length=255, blank=True)),
                ('number_of_casualties', models.CharField(default=b'0-10', max_length=255, choices=[(b'0-10', b'0-10'), (b'11-20', b'11-20'), (b'21-30', b'21-30')])),
                ('where_its_happend', models.CharField(max_length=255, null=True, blank=True)),
                ('created_by', models.ForeignKey(related_name='created_mir_registerincident_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('patient', models.ForeignKey(to='opal.Patient')),
                ('updated_by', models.ForeignKey(related_name='updated_mir_registerincident_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
        migrations.AddField(
            model_name='preincidentdata',
            name='country_fk',
            field=models.ForeignKey(blank=True, to='opal.Destination', null=True),
        ),
        migrations.AddField(
            model_name='preincidentdata',
            name='country_ft',
            field=models.CharField(default=b'', max_length=255, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='preincidentdata',
            name='discription_area_of_the_incident',
            field=models.TextField(null=True, verbose_name=b'Description of the area of the incident', blank=True),
        ),
        migrations.AddField(
            model_name='preincidentdata',
            name='discription_the_special_circumstances',
            field=models.TextField(null=True, verbose_name=b'Description of the area of the incident', blank=True),
        ),
        migrations.AddField(
            model_name='preincidentdata',
            name='more_than_one_country',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='mainauthor',
            name='role',
            field=models.TextField(null=True, verbose_name=b'Please describe which role the author had in the major incident', blank=True),
        ),
    ]
