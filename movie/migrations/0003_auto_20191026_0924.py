# Generated by Django 2.2.6 on 2019-10-26 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_auto_20191026_0919'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MovieLinks',
            new_name='MovieLink',
        ),
    ]
