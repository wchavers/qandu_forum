# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_vote'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Forum',
            new_name='Question',
        ),
        migrations.RenameField(
            model_name='vote',
            old_name='forum',
            new_name='question',
        ),
    ]
