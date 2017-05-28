# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mir', '0015_auto_20170528_1144'),
    ]

    operations = [
        migrations.RenameField(
            model_name='firstemergencyresponder',
            old_name='biological',
            new_name='cause_biological',
        ),
        migrations.RenameField(
            model_name='firstemergencyresponder',
            old_name='chemical',
            new_name='cause_chemical',
        ),
        migrations.RenameField(
            model_name='firstemergencyresponder',
            old_name='explosive',
            new_name='cause_explosive',
        ),
        migrations.RenameField(
            model_name='firstemergencyresponder',
            old_name='extreme_weather',
            new_name='cause_extreme_weather',
        ),
        migrations.RenameField(
            model_name='firstemergencyresponder',
            old_name='fire',
            new_name='cause_fire',
        ),
        migrations.RenameField(
            model_name='firstemergencyresponder',
            old_name='industrial_accident',
            new_name='cause_industrial_accident',
        ),
        migrations.RenameField(
            model_name='firstemergencyresponder',
            old_name='mass_gathering',
            new_name='cause_mass_gathering',
        ),
        migrations.RenameField(
            model_name='firstemergencyresponder',
            old_name='nuclear_radiological',
            new_name='cause_nuclear_radiological',
        ),
        migrations.RenameField(
            model_name='firstemergencyresponder',
            old_name='transport_industrial',
            new_name='cause_transport_industrial',
        ),
        migrations.RenameField(
            model_name='firstemergencyresponder',
            old_name='other_cause',
            new_name='specify_cause',
        ),
        migrations.RenameField(
            model_name='firstemergencyresponder',
            old_name='weather_type',
            new_name='specify_weather',
        ),
        migrations.RemoveField(
            model_name='firstemergencyresponder',
            name='authorisation_required',
        ),
        migrations.RemoveField(
            model_name='firstemergencyresponder',
            name='different_system',
        ),
        migrations.RemoveField(
            model_name='firstemergencyresponder',
            name='different_system_description',
        ),
        migrations.RemoveField(
            model_name='firstemergencyresponder',
            name='directly_referred',
        ),
        migrations.RemoveField(
            model_name='firstemergencyresponder',
            name='hospital_without_trauma_specialty',
        ),
        migrations.RemoveField(
            model_name='firstemergencyresponder',
            name='one_common_number',
        ),
        migrations.RemoveField(
            model_name='firstemergencyresponder',
            name='other_unknown',
        ),
        migrations.RemoveField(
            model_name='firstemergencyresponder',
            name='trauma_centres',
        ),
        migrations.RemoveField(
            model_name='firstemergencyresponder',
            name='trauma_units',
        ),
        migrations.RemoveField(
            model_name='firstemergencyresponder',
            name='triage_system',
        ),
        migrations.RemoveField(
            model_name='firstemergencyresponder',
            name='voluntary',
        ),
        migrations.RemoveField(
            model_name='firstemergencyresponder',
            name='which_triage_system',
        ),
        migrations.AddField(
            model_name='firstemergencyresponder',
            name='cause_other',
            field=models.BooleanField(default=False, verbose_name=b'Other / unknown'),
        ),
    ]
