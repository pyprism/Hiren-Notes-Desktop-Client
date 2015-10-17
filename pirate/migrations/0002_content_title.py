# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('pirate', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='title',
            field=models.CharField(max_length=200, default=datetime.datetime(2015, 10, 17, 11, 42, 17, 391395, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
