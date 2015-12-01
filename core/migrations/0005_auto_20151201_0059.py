# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20151117_2020'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='league',
            field=models.IntegerField(default=0, choices=[(0, b'Standard'), (1, b'.5 PPR'), (2, b' PPR')]),
        ),
        migrations.AddField(
            model_name='question',
            name='league',
            field=models.IntegerField(default=0, choices=[(0, b'Standard'), (1, b'.5 PPR'), (2, b' PPR')]),
        ),
    ]
