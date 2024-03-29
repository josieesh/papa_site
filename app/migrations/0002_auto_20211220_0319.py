# Generated by Django 3.1.5 on 2021-12-20 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='table',
            name='html',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='table',
            name='plaintext',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='heading1',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='heading2',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='heading3',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='heading4',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.DeleteModel(
            name='Textfile',
        ),
    ]
