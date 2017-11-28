# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_file_uploader', '0007_auto_20171128_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersharedfiles',
            name='file_id',
            field=models.IntegerField(),
        ),
    ]
