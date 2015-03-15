# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('decompile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apkfile',
            name='apkfile',
            field=models.FileField(upload_to=b''),
            preserve_default=True,
        ),
    ]
