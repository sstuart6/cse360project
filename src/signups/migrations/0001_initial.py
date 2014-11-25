# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('picture_name', models.CharField(max_length=120)),
                ('photo', models.ImageField(storage=b'/Users/ted123810/Desktop/practice/static/media', upload_to=b'')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('full_name', models.CharField(max_length=120)),
                ('password', models.CharField(max_length=120)),
                ('email', models.EmailField(unique=True, max_length=75, validators=[django.core.validators.EmailValidator()])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='picture',
            name='user_id',
            field=models.ForeignKey(related_name=b'pictures', to='signups.User'),
            preserve_default=True,
        ),
    ]
