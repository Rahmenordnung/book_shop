# Generated by Django 2.2.4 on 2019-08-21 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('literature', '0006_auto_20190821_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maestro',
            name='category',
            field=models.CharField(choices=[('HORROR', 'Horror'), ('LOVE', 'Love'), ('REALITY', 'Reality'), ('ADVENTURE', 'Adventure')], max_length=4),
        ),
    ]
