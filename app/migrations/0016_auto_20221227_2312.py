# Generated by Django 3.1.5 on 2022-12-27 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_auto_20221226_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='url_name',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
