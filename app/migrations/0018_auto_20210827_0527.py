# Generated by Django 3.1.5 on 2021-08-27 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_auto_20210825_0615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='page',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
