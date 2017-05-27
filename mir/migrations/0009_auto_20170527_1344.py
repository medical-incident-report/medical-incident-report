# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mir', '0008_auto_20170527_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bronzeofficer',
            name='biological',
            field=models.BooleanField(default=False, verbose_name=b'Biological'),
        ),
        migrations.AlterField(
            model_name='bronzeofficer',
            name='chemical',
            field=models.BooleanField(default=False, verbose_name=b'Chemical'),
        ),
        migrations.AlterField(
            model_name='bronzeofficer',
            name='explosive',
            field=models.BooleanField(default=False, verbose_name=b'Explosive'),
        ),
        migrations.AlterField(
            model_name='bronzeofficer',
            name='extreme_weather',
            field=models.BooleanField(default=False, verbose_name=b'Extreme weather'),
        ),
        migrations.AlterField(
            model_name='bronzeofficer',
            name='fire',
            field=models.BooleanField(default=False, verbose_name=b'Fire'),
        ),
        migrations.AlterField(
            model_name='bronzeofficer',
            name='industrial_accident',
            field=models.BooleanField(default=False, verbose_name=b'Industrial accident'),
        ),
        migrations.AlterField(
            model_name='bronzeofficer',
            name='mass_gathering',
            field=models.BooleanField(default=False, verbose_name=b'Mass Gathering'),
        ),
        migrations.AlterField(
            model_name='bronzeofficer',
            name='nuclear_radiological',
            field=models.BooleanField(default=False, verbose_name=b'Nuclear or radiological incident'),
        ),
        migrations.AlterField(
            model_name='bronzeofficer',
            name='other_unknown',
            field=models.BooleanField(default=False, verbose_name=b'Other/unknown'),
        ),
        migrations.AlterField(
            model_name='bronzeofficer',
            name='transport_industrial',
            field=models.BooleanField(default=False, verbose_name=b'Transport and industrial accident'),
        ),
    ]
