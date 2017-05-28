# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mir', '0016_auto_20170528_1158'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bronzeofficer',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='bronzeofficer',
            name='patient',
        ),
        migrations.RemoveField(
            model_name='bronzeofficer',
            name='updated_by',
        ),
        migrations.DeleteModel(
            name='BronzeOfficer',
        ),
    ]
