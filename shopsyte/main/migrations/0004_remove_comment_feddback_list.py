# Generated by Django 3.1.2 on 2020-10-31 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_comment_feddback_list'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='feddback_list',
        ),
    ]
