# Generated by Django 5.0.3 on 2024-04-25 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='age',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
