# Generated by Django 3.1.5 on 2022-12-26 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20220212_0401'),
    ]

    operations = [
        migrations.AddField(
            model_name='chaptertable',
            name='plaintext',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='heading1table',
            name='plaintext',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='heading2table',
            name='plaintext',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='heading3table',
            name='plaintext',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='heading4table',
            name='plaintext',
            field=models.TextField(blank=True, null=True),
        ),
    ]
