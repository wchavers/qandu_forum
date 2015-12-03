# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20151201_0059'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='league',
        ),
        migrations.AddField(
            model_name='vote',
            name='answer',
            field=models.ForeignKey(default='1', to='core.Answer'),
            preserve_default=False,
        ),
    ]
