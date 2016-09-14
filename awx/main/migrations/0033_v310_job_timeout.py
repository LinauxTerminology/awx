# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0032_v302_credential_permissions_update'),
    ]

    operations = [
        migrations.AddField(
            model_name='adhoccommand',
            name='timeout',
            field=models.PositiveIntegerField(default=0, blank=True),
        ),
        migrations.AddField(
            model_name='inventorysource',
            name='timeout',
            field=models.PositiveIntegerField(default=0, blank=True),
        ),
        migrations.AddField(
            model_name='inventoryupdate',
            name='timeout',
            field=models.PositiveIntegerField(default=0, blank=True),
        ),
        migrations.AddField(
            model_name='job',
            name='timeout',
            field=models.PositiveIntegerField(default=0, blank=True),
        ),
        migrations.AddField(
            model_name='jobtemplate',
            name='timeout',
            field=models.PositiveIntegerField(default=0, blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='timeout',
            field=models.PositiveIntegerField(default=0, blank=True),
        ),
        migrations.AddField(
            model_name='projectupdate',
            name='timeout',
            field=models.PositiveIntegerField(default=0, blank=True),
        ),
        migrations.AddField(
            model_name='systemjob',
            name='timeout',
            field=models.PositiveIntegerField(default=0, blank=True),
        ),
        migrations.AddField(
            model_name='systemjobtemplate',
            name='timeout',
            field=models.PositiveIntegerField(default=0, blank=True),
        ),
    ]
