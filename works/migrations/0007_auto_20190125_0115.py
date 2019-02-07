# Generated by Django 2.1.5 on 2019-01-24 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0006_auto_20190125_0054'),
    ]

    operations = [
        migrations.AddField(
            model_name='artist',
            name='artist_logo',
            field=models.FileField(default=None, upload_to=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='song',
            name='audio_track',
            field=models.FileField(upload_to=''),
        ),
    ]