# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mir', '0014_auto_20170528_1119'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bronzeofficer',
            name='biological',
        ),
        migrations.RemoveField(
            model_name='bronzeofficer',
            name='chemical',
        ),
        migrations.RemoveField(
            model_name='bronzeofficer',
            name='coupled_to_another',
        ),
        migrations.RemoveField(
            model_name='bronzeofficer',
            name='explosive',
        ),
        migrations.RemoveField(
            model_name='bronzeofficer',
            name='extreme_weather',
        ),
        migrations.RemoveField(
            model_name='bronzeofficer',
            name='fire',
        ),
        migrations.RemoveField(
            model_name='bronzeofficer',
            name='industrial_accident',
        ),
        migrations.RemoveField(
            model_name='bronzeofficer',
            name='mass_gathering',
        ),
        migrations.RemoveField(
            model_name='bronzeofficer',
            name='nuclear_radiological',
        ),
        migrations.RemoveField(
            model_name='bronzeofficer',
            name='other_cause',
        ),
        migrations.RemoveField(
            model_name='bronzeofficer',
            name='other_unknown',
        ),
        migrations.RemoveField(
            model_name='bronzeofficer',
            name='specify_copled',
        ),
        migrations.RemoveField(
            model_name='bronzeofficer',
            name='transport_industrial',
        ),
        migrations.RemoveField(
            model_name='bronzeofficer',
            name='weather_type',
        ),
        migrations.AddField(
            model_name='firstemergencyresponder',
            name='biological',
            field=models.BooleanField(default=False, verbose_name=b'Biological'),
        ),
        migrations.AddField(
            model_name='firstemergencyresponder',
            name='chemical',
            field=models.BooleanField(default=False, verbose_name=b'Chemical'),
        ),
        migrations.AddField(
            model_name='firstemergencyresponder',
            name='coupled_to_another',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name=b'Is this incident coupled to another incident?', choices=[(b'Yes', b'Yes'), (b'No', b'No')]),
        ),
        migrations.AddField(
            model_name='firstemergencyresponder',
            name='date_time',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='firstemergencyresponder',
            name='explosive',
            field=models.BooleanField(default=False, verbose_name=b'Explosive'),
        ),
        migrations.AddField(
            model_name='firstemergencyresponder',
            name='extreme_weather',
            field=models.BooleanField(default=False, verbose_name=b'Extreme weather'),
        ),
        migrations.AddField(
            model_name='firstemergencyresponder',
            name='fire',
            field=models.BooleanField(default=False, verbose_name=b'Fire'),
        ),
        migrations.AddField(
            model_name='firstemergencyresponder',
            name='industrial_accident',
            field=models.BooleanField(default=False, verbose_name=b'Industrial accident'),
        ),
        migrations.AddField(
            model_name='firstemergencyresponder',
            name='location_airport',
            field=models.BooleanField(default=False, verbose_name=b'Airport'),
        ),
        migrations.AddField(
            model_name='firstemergencyresponder',
            name='location_building',
            field=models.BooleanField(default=False, verbose_name=b'Building'),
        ),
        migrations.AddField(
            model_name='firstemergencyresponder',
            name='location_education',
            field=models.BooleanField(default=False, verbose_name=b'Education facility'),
        ),
        migrations.AddField(
            model_name='firstemergencyresponder',
            name='location_gathering',
            field=models.BooleanField(default=False, verbose_name=b'Mass gathering'),
        ),
        migrations.AddField(
            model_name='firstemergencyresponder',
            name='location_healthcare',
            field=models.BooleanField(default=False, verbose_name=b'Health care facility'),
        ),
        migrations.AddField(
            model_name='firstemergencyresponder',
            name='location_maritime',
            field=models.BooleanField(default=False, verbose_name=b'Offshore/maritine (ocean, river, lake)'),
        ),
        migrations.AddField(
            model_name='firstemergencyresponder',
            name='location_mountain',
            field=models.BooleanField(default=False, verbose_name=b'Mountain'),
        ),
        migrations.AddField(
            model_name='firstemergencyresponder',
            name='location_other',
            field=models.BooleanField(default=False, verbose_name=b'Other / unknown'),
        ),
        migrations.AddField(
            model_name='firstemergencyresponder',
            name='location_public',
            field=models.BooleanField(default=False, verbose_name=b'Public facility'),
        ),
        migrations.AddField(
            model_name='firstemergencyresponder',
            name='location_road',
            field=models.BooleanField(default=False, verbose_name=b'Road'),
        ),
        migrations.AddField(
            model_name='firstemergencyresponder',
            name='location_rural',
            field=models.BooleanField(default=False, verbose_name=b'Rural/countryside area'),
        ),
        migrations.AddField(
            model_name='firstemergencyresponder',
            name='location_urban',
            field=models.BooleanField(default=False, verbose_name=b'Urban area'),
        ),
        migrations.AddField(
            model_name='firstemergencyresponder',
            name='mass_gathering',
            field=models.BooleanField(default=False, verbose_name=b'Mass Gathering'),
        ),
        migrations.AddField(
            model_name='firstemergencyresponder',
            name='nuclear_radiological',
            field=models.BooleanField(default=False, verbose_name=b'Nuclear or radiological incident'),
        ),
        migrations.AddField(
            model_name='firstemergencyresponder',
            name='other_cause',
            field=models.TextField(null=True, verbose_name=b'Please specify other mechanism/external factor that caused the incident', blank=True),
        ),
        migrations.AddField(
            model_name='firstemergencyresponder',
            name='other_unknown',
            field=models.BooleanField(default=False, verbose_name=b'Other/unknown'),
        ),
        migrations.AddField(
            model_name='firstemergencyresponder',
            name='specify_coupled',
            field=models.TextField(null=True, verbose_name=b'Please specify which other incident this major incident is coupled to', blank=True),
        ),
        migrations.AddField(
            model_name='firstemergencyresponder',
            name='specify_location',
            field=models.TextField(null=True, verbose_name=b'Please specify which other type of location of incident scene', blank=True),
        ),
        migrations.AddField(
            model_name='firstemergencyresponder',
            name='transport_industrial',
            field=models.BooleanField(default=False, verbose_name=b'Transport and industrial accident'),
        ),
        migrations.AddField(
            model_name='firstemergencyresponder',
            name='weather_type',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name=b'Please specify the extreme weather that caused the incident', choices=[(b'Avalance', b'Avalanche'), (b'Flooding', b'Flooding'), (b'Thunderstorm', b'Thunderstorm'), (b'Hurricane', b'Hurricaine'), (b'Extreme heat', b'Extreme heat'), (b'Extreme cold', b'Extreme cold'), (b'Other type of extreme weather. Please specify', b'Other types of extreme weather. Please specify')]),
        ),
    ]
