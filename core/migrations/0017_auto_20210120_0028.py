# Generated by Django 3.1.4 on 2021-01-20 05:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20210118_0028'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='game',
            new_name='favorite_game',
        ),
    ]
