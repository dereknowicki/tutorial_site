# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TutURLcomment',
            fields=[
                ('tutcomment_ptr', models.OneToOneField(parent_link=True, serialize=False, to='tutorials.TutComment', primary_key=True, auto_created=True)),
                ('link', models.URLField(max_length=2000, blank=True)),
            ],
            bases=('tutorials.tutcomment',),
        ),
    ]
