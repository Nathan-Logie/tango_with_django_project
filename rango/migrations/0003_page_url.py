# Generated by Django 2.2.28 on 2023-01-30 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_auto_20230130_0853'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='url',
            field=models.URLField(default='DEFAULT'),
            preserve_default=False,
        ),
    ]
