# Generated by Django 3.1.5 on 2021-12-21 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20211221_0449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='heading1',
            name='name',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
