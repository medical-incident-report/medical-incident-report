# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mir', '0013_auto_20170528_1013'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registerincident',
            name='date_time',
        ),
        migrations.RemoveField(
            model_name='registerincident',
            name='link_to_the_newsfeed',
        ),
        migrations.RemoveField(
            model_name='registerincident',
            name='number_of_casualties',
        ),
    ]
