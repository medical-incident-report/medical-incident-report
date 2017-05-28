# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mir', '0013_auto_20170528_1013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bronzeofficer',
            name='coupled_to_another',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name=b'Is this incident coupled to another incident?', choices=[(b'Yes', b'Yes'), (b'No', b'No')]),
        ),
    ]
