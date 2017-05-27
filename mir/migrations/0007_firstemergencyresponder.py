# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import opal.models


class Migration(migrations.Migration):

    dependencies = [
        ('opal', '0028_auto_20170210_1146'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mir', '0006_auto_20170527_1119'),
    ]

    operations = [
        migrations.CreateModel(
            name='FirstEmergencyResponder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('updated', models.DateTimeField(null=True, blank=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('one_common_number', models.CharField(default=b'Yes', max_length=256, verbose_name=b'Is there one common phone number for the emergency services?', choices=[(b'Yes', b'Yes'), (b'No', b'No')])),
                ('directly_referred', models.CharField(default=b'Yes', max_length=256, verbose_name=b'Can an emergency incident be referred directly by the EMS?', choices=[(b'Yes', b'Yes'), (b'No', b'No')])),
                ('voluntary', models.TextField(null=True, verbose_name=b'Which voluntary organisations can assist the EMS?', blank=True)),
                ('authorisation_required', models.CharField(max_length=256, verbose_name=b'Do they require authorisation from the police?', choices=[(b'Yes', b'Yes'), (b'No', b'No')])),
                ('trauma_centres', models.IntegerField(null=True, verbose_name=b'Please enter the number of major trauma centres within the EMS catchment zone?', blank=True)),
                ('trauma_units', models.IntegerField(null=True, verbose_name=b'Please enter the number of major trauma units within the EMS catchment zone?', blank=True)),
                ('hospital_without_trauma_specialty', models.IntegerField(null=True, verbose_name=b'Please enter the number of hospitals without trauma specialty within the EMS catchment zone?', blank=True)),
                ('triage_system', models.CharField(default=False, max_length=256, verbose_name=b'Is a prehospital on scene triage system being used daily on a national level?', choices=[(b'Yes', b'Yes'), (b'No', b'No')])),
                ('which_triage_system', models.CharField(blank=True, max_length=256, null=True, verbose_name=b'Please specify which prehospital on scene triage system is being used', choices=[(b'Yes', b'Yes'), (b'No', b'No')])),
                ('different_system', models.CharField(blank=True, max_length=256, null=True, verbose_name=b'Is the system used on a daily basis the same as the one used in a major incident', choices=[(b'Yes', b'Yes'), (b'No', b'No')])),
                ('different_system_description', models.TextField(verbose_name=b'If not what is it?')),
                ('created_by', models.ForeignKey(related_name='created_mir_firstemergencyresponder_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('patient', models.ForeignKey(to='opal.Patient')),
                ('updated_by', models.ForeignKey(related_name='updated_mir_firstemergencyresponder_subrecords', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
    ]
