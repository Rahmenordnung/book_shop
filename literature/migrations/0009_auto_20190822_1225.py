# Generated by Django 2.2.4 on 2019-08-22 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('literature', '0008_auto_20190822_1204'),
    ]

    operations = [
        migrations.RenameField(
            model_name='work',
            old_name='slug',
            new_name='slug_description',
        ),
    ]