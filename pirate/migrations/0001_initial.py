# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('content', models.TextField()),
                ('date', models.DateField(auto_now_add=True)),
                ('slug', models.CharField(unique=True, max_length=150)),
                ('category', models.CharField(max_length=10, choices=[('MOVIE', 'Movie'), ('SONG', 'Song'), ('LIFESTYLE', 'LifeStyle'), ('TECH', 'Technology')])),
            ],
        ),
        migrations.CreateModel(
            name='Latest',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('reference', models.ForeignKey(to='pirate.Content')),
            ],
        ),
    ]
