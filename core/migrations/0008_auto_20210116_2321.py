# Generated by Django 3.1.4 on 2021-01-17 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20210116_2320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='image',
            field=models.ImageField(blank=True, upload_to='core/game'),
        ),
    ]
