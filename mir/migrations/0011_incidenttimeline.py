# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import opal.models


class Migration(migrations.Migration):

    dependencies = [
        ('opal', '0028_auto_20170210_1146'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mir', '0010_auto_20170527_1412'),
    ]

    operations = [
        migrations.CreateModel(
            name='IncidentTimeline',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('updated', models.DateTimeField(null=True, blank=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('incident_occurs', models.DateTimeField(null=True, verbose_name=b'Time incident occurred', blank=True)),
                ('first_ems_call', models.DateTimeField(null=True, verbose_name=b'Initial call to emergency services EOC', blank=True)),
                ('first_ems_response', models.DateTimeField(null=True, verbose_name=b'First EMS response vehicle arrives on scene', blank=True)),
                ('first_police_response', models.DateTimeField(null=True, verbose_name=b'First Police arrive on scene', blank=True)),
                ('first_fire_response', models.DateTimeField(null=True, verbose_name=b'First Fire services arrive on scene', blank=True)),
                ('med_commander', models.DateTimeField(null=True, verbose_name=b'Medical responder assumes the role of on-scene medical commander', blank=True)),
                ('safety_assessment_start', models.DateTimeField(null=True, verbose_name=b'Medical responder begins to make an assessment of scene safety', blank=True)),
                ('report_to_ems', models.DateTimeField(null=True, verbose_name=b'Medical responder communicates a situation report to EMS coordination centre', blank=True)),
                ('resource_request', models.DateTimeField(null=True, verbose_name=b'Medical responder requests additional resources', blank=True)),
                ('safety_action', models.DateTimeField(null=True, verbose_name=b'Medical responder initiates any safety related actions', blank=True)),
                ('delegation', models.DateTimeField(null=True, verbose_name=b'Medical responder delegates responsibility for other tasks on-scene', blank=True)),
                ('ems_officer_arrives', models.DateTimeField(null=True, verbose_name=b'First EMS officer arrives on scene', blank=True)),
                ('ems_officer_commands', models.DateTimeField(null=True, verbose_name=b'First EMS officer assumes role of medical commander', blank=True)),
                ('mi_declared', models.DateTimeField(null=True, verbose_name=b'EMS declares a major incident', blank=True)),
                ('summon_staff', models.DateTimeField(null=True, verbose_name=b'Summoning of additional medica staff to scene', blank=True)),
                ('clearning_start', models.DateTimeField(null=True, verbose_name=b'Casualty Clearing Station established', blank=True)),
                ('hospital_informed', models.DateTimeField(null=True, verbose_name=b'Hospital informed of major incident', blank=True)),
                ('hospital_declares', models.DateTimeField(null=True, verbose_name=b'Hospital declares major incident', blank=True)),
                ('first_patient_evacuated', models.DateTimeField(null=True, verbose_name=b'First patient evacuated from scene', blank=True)),
                ('first_patient_arrives', models.DateTimeField(null=True, verbose_name=b'First patient arrives at hospital', blank=True)),
                ('medical_communication', models.DateTimeField(null=True, verbose_name=b'Communication between medical personell at the incident initiated', blank=True)),
                ('task_force_communication', models.DateTimeField(null=True, verbose_name=b'Communication between different task forces (e.g. police, fire) initiated', blank=True)),
                ('last_patient_evacuated', models.DateTimeField(null=True, verbose_name=b'Last patient evacuated from scene', blank=True)),
                ('last_patient_arrives', models.DateTimeField(null=True, verbose_name=b'Last patient arrives at hospital', blank=True)),
                ('mi_stand_down_ems', models.DateTimeField(null=True, verbose_name=b'Major incident stand down declared by EMS', blank=True)),
                ('mi_stand_down_hospital', models.DateTimeField(null=True, verbose_name=b'Major incident stand down declared by hospital', blank=True)),
                ('created_by', models.ForeignKey(related_name='created_mir_incidenttimeline_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('patient', models.ForeignKey(to='opal.Patient')),
                ('updated_by', models.ForeignKey(related_name='updated_mir_incidenttimeline_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
    ]
