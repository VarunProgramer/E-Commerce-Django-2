# Generated by Django 4.2.3 on 2023-08-17 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Exchenger', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codegery',
            name='description',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='prodect',
            name='description',
            field=models.TextField(max_length=500),
        ),
    ]