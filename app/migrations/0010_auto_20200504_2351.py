# Generated by Django 3.0.5 on 2020-05-04 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_textfile_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textfile',
            name='category',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
