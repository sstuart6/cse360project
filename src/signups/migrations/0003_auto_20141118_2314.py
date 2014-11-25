# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.files.storage


class Migration(migrations.Migration):

    dependencies = [
        ('signups', '0002_remove_picture_picture_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='photo',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(location=b'/Users/ted123810/Desktop/practice/static/media'), upload_to=b''),
        ),
    ]
