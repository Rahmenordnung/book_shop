# Generated by Django 2.2.4 on 2019-08-27 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('literature', '0020_auto_20190827_1044'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='work',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
