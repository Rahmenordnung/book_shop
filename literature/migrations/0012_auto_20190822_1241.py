# Generated by Django 2.2.4 on 2019-08-22 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('literature', '0011_auto_20190822_1240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='description',
            field=models.CharField(max_length=630),
        ),
    ]