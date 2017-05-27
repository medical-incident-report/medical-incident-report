# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import opal.models


class Migration(migrations.Migration):

    dependencies = [
        ('opal', '0028_auto_20170210_1146'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mir', '0007_firstemergencyresponder'),
    ]

    operations = [
        migrations.CreateModel(
            name='BronzeOfficer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('updated', models.DateTimeField(null=True, blank=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('transport_industrial', models.BooleanField(verbose_name=b'Transport and industrial accident')),
                ('extreme_weather', models.BooleanField(verbose_name=b'Extreme weather')),
                ('fire', models.BooleanField(verbose_name=b'Fire')),
                ('mass_gathering', models.BooleanField(verbose_name=b'Mass Gathering')),
                ('explosive', models.BooleanField(verbose_name=b'Explosive')),
                ('industrial_accident', models.BooleanField(verbose_name=b'Industrial accident')),
                ('nuclear_radiological', models.BooleanField(verbose_name=b'Nuclear or radiological incident')),
                ('biological', models.BooleanField(verbose_name=b'Biological')),
                ('chemical', models.BooleanField(verbose_name=b'Chemical')),
                ('other_unknown', models.BooleanField(verbose_name=b'Other/unknown')),
                ('weather_type', models.CharField(blank=True, max_length=256, null=True, verbose_name=b'Please specify the extreme weather that caused the incident', choices=[(b'Avalance', b'Avalanche'), (b'Flooding', b'Flooding'), (b'Thunderstorm', b'Thunderstorm'), (b'Hurricaine', b'Hurricaine'), (b'Extreme heat', b'Extreme heat'), (b'Extreme cold', b'Extreme cold'), (b'Other type of extreme weather. Please specify', b'Other types of extreme weather. Please specify')])),
                ('other_cause', models.TextField(null=True, verbose_name=b'Please specify other mechanism/external factor that caused the incident', blank=True)),
                ('coupled_to_another', models.CharField(max_length=256, verbose_name=b'Is this incident coupled to another incident?', choices=[(b'Yes', b'Yes'), (b'No', b'No')])),
                ('specify_copled', models.TextField(null=True, verbose_name=b'Please specify which other incident this major incident is coupled to', blank=True)),
                ('created_by', models.ForeignKey(related_name='created_mir_bronzeofficer_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('patient', models.ForeignKey(to='opal.Patient')),
                ('updated_by', models.ForeignKey(related_name='updated_mir_bronzeofficer_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
        migrations.AddField(
            model_name='registerincident',
            name='date_time',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
