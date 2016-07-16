# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='description',
            field=models.TextField(default=b'Product Description'),
        ),
        migrations.AddField(
            model_name='products',
            name='price',
            field=models.DecimalField(default=0.0, max_digits=7, decimal_places=2),
        ),
    ]
