# Generated by Django 3.1.5 on 2021-12-21 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_heading1_is_html'),
    ]

    operations = [
        migrations.AddField(
            model_name='heading2',
            name='is_html',
            field=models.BooleanField(default=False, verbose_name='Turn text into HTML'),
        ),
        migrations.AddField(
            model_name='heading3',
            name='is_html',
            field=models.BooleanField(default=False, verbose_name='Turn text into HTML'),
        ),
        migrations.AddField(
            model_name='heading4',
            name='is_html',
            field=models.BooleanField(default=False, verbose_name='Turn text into HTML'),
        ),
        migrations.AlterField(
            model_name='chapter',
            name='is_html',
            field=models.BooleanField(default=False, verbose_name='Turn text into HTML'),
        ),
        migrations.AlterField(
            model_name='heading1',
            name='is_html',
            field=models.BooleanField(default=False, verbose_name='Turn text into HTML'),
        ),
    ]
