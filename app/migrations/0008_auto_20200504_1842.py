# Generated by Django 3.0.5 on 2020-05-04 18:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20200504_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='textfile',
            name='parent_page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='app.Textfile'),
        ),
    ]
