# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opal', '0028_auto_20170210_1146'),
        ('mir', '0011_incidenttimeline'),
    ]

    operations = [
        migrations.AddField(
            model_name='preincidentdata',
            name='countries',
            field=models.ManyToManyField(related_name='incident_countries', to='opal.Destination'),
        ),
    ]
