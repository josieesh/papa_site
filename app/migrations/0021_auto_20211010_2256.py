# Generated by Django 3.1.5 on 2021-10-10 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_auto_20210828_2329'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='url_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='heading1',
            name='url_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='heading2',
            name='url_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='heading3',
            name='url_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='heading4',
            name='url_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='table',
            name='url_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
