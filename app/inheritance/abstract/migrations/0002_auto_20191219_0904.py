# Generated by Django 2.2.9 on 2019-12-19 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abstract', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='age',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='name',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]
