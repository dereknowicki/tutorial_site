# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tutorials.models
from django.conf import settings
import sortedm2m.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TutComment',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Tutorial',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TutImageComment',
            fields=[
                ('tutcomment_ptr', models.OneToOneField(auto_created=True, to='tutorials.TutComment', primary_key=True, parent_link=True, serialize=False)),
                ('photo', models.ImageField(upload_to=tutorials.models.content_file_name)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, default='derek')),
            ],
            bases=('tutorials.tutcomment',),
        ),
        migrations.AddField(
            model_name='tutorial',
            name='comments',
            field=sortedm2m.fields.SortedManyToManyField(help_text=None, to='tutorials.TutComment', blank=True),
        ),
        migrations.AddField(
            model_name='tutorial',
            name='subtuts',
            field=sortedm2m.fields.SortedManyToManyField(help_text=None, to='tutorials.Tutorial', blank=True),
        ),
    ]
