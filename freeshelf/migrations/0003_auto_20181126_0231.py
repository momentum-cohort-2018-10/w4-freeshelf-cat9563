# Generated by Django 2.1 on 2018-11-26 02:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('freeshelf', '0002_categories'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categories',
            new_name='Category',
        ),
    ]
