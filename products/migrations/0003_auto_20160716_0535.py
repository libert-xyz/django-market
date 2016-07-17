# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20160716_0514'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=40)),
                ('price', models.DecimalField(default=0.0, max_digits=7, decimal_places=2)),
                ('description', models.TextField(default=b'Product Description')),
            ],
        ),
        migrations.DeleteModel(
            name='Products',
        ),
    ]
