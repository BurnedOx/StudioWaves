# Generated by Django 2.1.5 on 2019-02-04 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('works', '0008_gallery'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=10000)),
            ],
        ),
    ]
