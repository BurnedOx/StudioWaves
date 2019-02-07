# Generated by Django 2.1.5 on 2019-01-23 05:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Single_Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_title', models.CharField(max_length=250)),
                ('file_type', models.CharField(max_length=10)),
                ('genre', models.CharField(max_length=100)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='works.Artist')),
            ],
        ),
        migrations.RenameModel(
            old_name='Song',
            new_name='Album_Song',
        ),
    ]
