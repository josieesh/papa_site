# Generated by Django 3.1.5 on 2021-08-23 07:09

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('app', '0015_auto_20210630_0308'),
    ]

    operations = [
        migrations.CreateModel(
            name='Heading1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('text', models.TextField(blank=True, null=True)),
                ('order', models.IntegerField(default=1)),
                ('date_added', models.DateTimeField(default=datetime.datetime.now, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='textfile',
            name='tags',
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
            ],
        ),
        migrations.CreateModel(
            name='Heading2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('parent_heading', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.heading1')),
            ],
        ),
        migrations.AddField(
            model_name='heading1',
            name='page',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.page'),
        ),
    ]
