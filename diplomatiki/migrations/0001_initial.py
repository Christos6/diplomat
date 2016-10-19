# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('activity_id', models.AutoField(serialize=False, primary_key=True)),
                ('activity_name', models.CharField(max_length=200)),
                ('activity_description', models.CharField(default=b'', max_length=500)),
                ('icon', models.CharField(default=b'', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='acts',
            fields=[
                ('acts_id', models.AutoField(serialize=False, primary_key=True)),
                ('acts_goal', models.CharField(max_length=200)),
                ('acts_goal_status', models.CharField(max_length=20, null=True, choices=[(b'Reached', b'Reached'), (b'Inprogress', b'In progress'), (b'Failed', b'Failed')])),
                ('astart_date', models.DateTimeField(verbose_name=b'Start time')),
                ('aend_date', models.DateTimeField(verbose_name=b'End time')),
                ('activitay', models.ForeignKey(to='diplomatiki.Activity', db_column=b'Activity_key')),
                ('man', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Frenemy',
            fields=[
                ('Frenemy_id', models.AutoField(serialize=False, primary_key=True)),
                ('Frenemy_name', models.CharField(max_length=100)),
                ('Frenemy_of_user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Thing',
            fields=[
                ('thing_name', models.CharField(max_length=100)),
                ('thing_id', models.AutoField(serialize=False, primary_key=True)),
                ('thing_of_user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='acts',
            name='withusing',
            field=models.ManyToManyField(to='diplomatiki.Thing'),
        ),
    ]
