# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tutorials.models
import sortedm2m.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TutComment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Tutorial',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('subtuts', sortedm2m.fields.SortedManyToManyField(to='tutorials.Tutorial', blank=True, help_text=None)),
            ],
        ),
        migrations.CreateModel(
            name='TutImageComment',
            fields=[
                ('tutcomment_ptr', models.OneToOneField(parent_link=True, serialize=False, auto_created=True, to='tutorials.TutComment', primary_key=True)),
                ('photo', models.ImageField(upload_to=tutorials.models.content_file_name, blank=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, default='derek')),
            ],
            bases=('tutorials.tutcomment',),
        ),
        migrations.CreateModel(
            name='TutUrlComment',
            fields=[
                ('tutcomment_ptr', models.OneToOneField(parent_link=True, serialize=False, auto_created=True, to='tutorials.TutComment', primary_key=True)),
                ('link', models.URLField(blank=True, max_length=2000)),
            ],
            bases=('tutorials.tutcomment',),
        ),
        migrations.AddField(
            model_name='tutorial',
            name='tut_comms',
            field=sortedm2m.fields.SortedManyToManyField(to='tutorials.TutComment', blank=True, help_text=None),
        ),
    ]
