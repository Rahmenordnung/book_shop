# Generated by Django 2.2.4 on 2019-08-27 13:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(default='', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Maestro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completename', models.CharField(max_length=50)),
                ('country_maestro', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('part_number', models.IntegerField()),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('publication_date', models.DateTimeField()),
                ('views', models.IntegerField(default=0)),
                ('description', models.CharField(max_length=630)),
                ('slug', models.SlugField()),
                ('cover', models.ImageField(upload_to='')),
                ('price', models.FloatField()),
                ('bestseller', models.BooleanField(default=False)),
                ('longbook', models.BooleanField(default=False)),
                ('worldwide_appreciated', models.BooleanField(default=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='literature.Category')),
                ('maestros', models.ManyToManyField(to='literature.Maestro')),
            ],
        ),
        migrations.CreateModel(
            name='UserLibrary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('works_owned', models.ManyToManyField(blank=True, to='literature.Work')),
            ],
            options={
                'verbose_name': 'User Library',
                'verbose_name_plural': 'User Library',
            },
        ),
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_number', models.IntegerField()),
                ('text_page_number', models.IntegerField()),
                ('title', models.CharField(max_length=50)),
                ('part', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='literature.Part')),
            ],
        ),
        migrations.AddField(
            model_name='part',
            name='work',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='literature.Work'),
        ),
        migrations.CreateModel(
            name='Essay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('essay_number', models.IntegerField()),
                ('image', models.ImageField(upload_to='')),
                ('text', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='literature.Text')),
            ],
        ),
    ]
