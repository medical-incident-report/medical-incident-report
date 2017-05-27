# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mir', '0009_auto_20170527_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bronzeofficer',
            name='weather_type',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name=b'Please specify the extreme weather that caused the incident', choices=[(b'Avalance', b'Avalanche'), (b'Flooding', b'Flooding'), (b'Thunderstorm', b'Thunderstorm'), (b'Hurricane', b'Hurricaine'), (b'Extreme heat', b'Extreme heat'), (b'Extreme cold', b'Extreme cold'), (b'Other type of extreme weather. Please specify', b'Other types of extreme weather. Please specify')]),
        ),
    ]
