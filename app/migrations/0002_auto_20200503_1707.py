# Generated by Django 3.0.5 on 2020-05-03 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textfile',
            name='tags',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
    ]
