# Generated by Django 3.1.5 on 2023-01-02 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_auto_20230102_0226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='order',
            field=models.IntegerField(blank=True, unique=True),
        ),
    ]