# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.files.storage
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_auto_20160727_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='media',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(location=b'/home/tux/Documents/repositories/django-market/static_cdn/protected'), null=True, upload_to=products.models.download_media_location, blank=True),
        ),
    ]
