# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opal', '0028_auto_20170210_1146'),
        ('mir', '0002_mainauthor_preincidentdata'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mainauthor',
            name='birth_place_fk',
        ),
        migrations.RemoveField(
            model_name='mainauthor',
            name='birth_place_ft',
        ),
        migrations.AddField(
            model_name='preincidentdata',
            name='country_fk',
            field=models.ForeignKey(blank=True, to='opal.Destination', null=True),
        ),
        migrations.AddField(
            model_name='preincidentdata',
            name='country_ft',
            field=models.CharField(default=b'', max_length=255, null=True, blank=True),
        ),
    ]
