# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opal', '0028_auto_20170210_1146'),
        ('mir', '0012_preincidentdata_countries'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mainauthor',
            name='country_fk',
        ),
        migrations.RemoveField(
            model_name='mainauthor',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='mainauthor',
            name='patient',
        ),
        migrations.RemoveField(
            model_name='mainauthor',
            name='title_fk',
        ),
        migrations.RemoveField(
            model_name='mainauthor',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='preincidentdata',
            name='countries',
        ),
        migrations.RemoveField(
            model_name='preincidentdata',
            name='country_fk',
        ),
        migrations.RemoveField(
            model_name='preincidentdata',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='preincidentdata',
            name='patient',
        ),
        migrations.RemoveField(
            model_name='preincidentdata',
            name='updated_by',
        ),
        migrations.AddField(
            model_name='registerincident',
            name='countries',
            field=models.ManyToManyField(related_name='incident_countries', verbose_name=b'In which countries did it happen?', to='opal.Destination'),
        ),
        migrations.DeleteModel(
            name='MainAuthor',
        ),
        migrations.DeleteModel(
            name='PreIncidentData',
        ),
    ]
