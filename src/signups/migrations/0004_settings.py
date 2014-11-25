# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.files.storage
import signups.models


class Migration(migrations.Migration):

    dependencies = [
        ('signups', '0003_auto_20141118_2314'),
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('profile_pic', models.ImageField(storage=django.core.files.storage.FileSystemStorage(location=b'/Users/ted123810/Desktop/practice/static/profile_pic'), upload_to=signups.models.get_profile_pic_name)),
                ('user', models.ForeignKey(related_name=b'settings', to='signups.User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
