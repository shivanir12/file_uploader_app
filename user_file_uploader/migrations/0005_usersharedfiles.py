# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_file_uploader', '0004_remove_file_updated_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSharedFiles',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file_id', models.IntegerField(max_length=100)),
                ('requested_user_id', models.IntegerField(max_length=200)),
                ('shared_user_id', models.IntegerField(max_length=200)),
            ],
        ),
    ]
