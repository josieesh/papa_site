# Generated by Django 3.1.5 on 2021-08-28 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_page_url_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='heading2',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='heading3',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='heading4',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
    ]