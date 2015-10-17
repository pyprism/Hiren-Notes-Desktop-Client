# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pirate', '0002_content_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='category',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='content',
            name='title',
            field=models.CharField(max_length=150),
        ),
    ]
