# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mir', '0005_auto_20170527_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registerincident',
            name='number_of_casualties',
            field=models.CharField(blank=True, max_length=255, null=True, choices=[(b'0-10', b'0-10'), (b'11-20', b'11-20'), (b'21-30', b'21-30')]),
        ),
    ]
