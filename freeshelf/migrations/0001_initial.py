# Generated by Django 2.1 on 2018-11-21 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('slug', models.SlugField(unique=True)),
                ('date', models.DateField()),
                ('url', models.URLField()),
            ],
        ),
    ]