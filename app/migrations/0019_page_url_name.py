# Generated by Django 3.1.5 on 2021-08-27 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_auto_20210827_0527'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='url_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]