# Generated by Django 2.2.4 on 2019-08-27 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('literature', '0026_auto_20190827_1137'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='work',
            name='bestseller',
        ),
        migrations.RemoveField(
            model_name='work',
            name='longbook',
        ),
        migrations.RemoveField(
            model_name='work',
            name='worldwide_appreciated',
        ),
    ]
