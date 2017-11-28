# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_file_uploader', '0005_usersharedfiles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersharedfiles',
            name='file_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='usersharedfiles',
            name='requested_user_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='usersharedfiles',
            name='shared_user_id',
            field=models.IntegerField(),
        ),
    ]
