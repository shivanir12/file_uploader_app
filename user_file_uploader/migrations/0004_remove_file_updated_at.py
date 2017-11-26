# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_file_uploader', '0003_file_file_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='updated_at',
        ),
    ]
