# Generated by Django 4.2.4 on 2023-08-30 05:03

import Exchenger.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Exchenger', '0003_prodect_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codegery',
            name='codegery_image',
            field=models.ImageField(blank=True, null=True, upload_to=Exchenger.models.getfilename),
        ),
        migrations.AlterField(
            model_name='prodect',
            name='more_prodect_image',
            field=models.ImageField(blank=True, null=True, upload_to=Exchenger.models.getfilename),
        ),
        migrations.AlterField(
            model_name='prodect',
            name='price',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='prodect',
            name='prodect_image',
            field=models.ImageField(blank=True, null=True, upload_to=Exchenger.models.getfilename),
        ),
    ]
