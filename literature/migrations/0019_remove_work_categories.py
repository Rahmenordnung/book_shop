# Generated by Django 2.2.4 on 2019-08-26 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('literature', '0018_auto_20190826_1244'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='work',
            name='categories',
        ),
    ]
