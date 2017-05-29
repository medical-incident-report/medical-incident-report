# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import opal.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('opal', '0028_auto_20170210_1146'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mir', '0017_auto_20170528_1331'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmsBackground',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('updated', models.DateTimeField(null=True, blank=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('ems_coordinating_centre_exists', models.CharField(blank=True, max_length=256, null=True, verbose_name=b'Was an EMS coordinating centre (the centre responsible for dispatching and coordinating EMS units to the scene) available in the affected country/ies at the time of the incident?', choices=[(b'Yes', b'Yes'), (b'No', b'No')])),
                ('ems_common_dialing_number', models.CharField(blank=True, max_length=256, null=True, verbose_name=b'Is there one common dialling number for all Emergency Services (fire, police, EMS)?', choices=[(b'Yes', b'Yes'), (b'No', b'No')])),
                ('ems_directly_declared', models.CharField(blank=True, max_length=256, null=True, verbose_name=b'Can a major incident be declared directly by the person receiving an alert at the EMS coordinating centre?', choices=[(b'Yes', b'Yes'), (b'No', b'No'), (b'Unknown', b'Unknown')])),
                ('basic_life_support_non_ems', models.BooleanField(default=False, verbose_name=b'Basic Life Support by EMS professional')),
                ('non_physician_advanced_live_support', models.BooleanField(default=False, verbose_name=b'non-physician Advanced Life Support by EMS professional')),
                ('life_support_on_scene_by_physician', models.BooleanField(default=False, verbose_name=b'Advanced Life Support by On-scene Physician')),
                ('other', models.CharField(max_length=256, null=True, blank=True)),
                ('voluntary_organisations_available', models.CharField(max_length=256, null=True, verbose_name=b'Please specify which voluntary organizations are available to assist the EMS service in a normal setting?', blank=True)),
                ('trauma_network', models.CharField(blank=True, max_length=256, null=True, verbose_name=b'Does the country where the major incident took place have a trauma network?', choices=[(b'Yes', b'Yes'), (b'No', b'No'), (b'Unknown', b'Unknown')])),
                ('regional_trauma_hospitals', models.BooleanField(default=False, verbose_name=b'Are there any regional hospital/s with trauma specialty that exists within the EMS catchment system that was affected by the major incident?')),
                ('pre_hospital_triage_system', models.CharField(blank=True, max_length=256, null=True, verbose_name=b'Is a pre-hospital triage system in use on a daily basis on regional levels?', choices=[(b'Yes', b'Yes'), (b'Yes, but different triage systems exist in different regions', b'Yes, but different triage systems exist in different regions'), (b'No', b'No'), (b'Unknown', b'Unknown')])),
                ('pre_hospital_triage_regional', models.CharField(blank=True, max_length=256, null=True, verbose_name=b'Is a pre-hospital triage system in use for major incidents on regional levels?', choices=[(b'Yes', b'Yes'), (b'Yes, but different triage systems exist in different region', b'Yes, but different triage systems exist in different region'), (b'No', b'No'), (b'Unknown', b'Unknown')])),
                ('regional_response_plan_including_all_emergency_services', models.CharField(blank=True, max_length=256, null=True, verbose_name=b'Is there a regional major incident response plan incorporating all emergency services within the area that the the major incident occured?', choices=[(b'Yes', b'Yes'), (b'No', b'No'), (b'Unknown', b'Unknown')])),
                ('created_by', models.ForeignKey(related_name='created_mir_emsbackground_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('patient', models.ForeignKey(to='opal.Patient')),
                ('updated_by', models.ForeignKey(related_name='updated_mir_emsbackground_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
        migrations.CreateModel(
            name='IncidentPlanQuestions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('updated', models.DateTimeField(null=True, blank=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('prehospital_major_incident_plan', models.TextField(verbose_name=b'Please Enter the pre-hospital major incident response if one exists?')),
                ('actual_response', models.TextField(verbose_name=b'ow did your actual response differ to the plan and what was the consequence of that?')),
                ('created_by', models.ForeignKey(related_name='created_mir_incidentplanquestions_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('patient', models.ForeignKey(to='opal.Patient')),
                ('updated_by', models.ForeignKey(related_name='updated_mir_incidentplanquestions_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
    ]
