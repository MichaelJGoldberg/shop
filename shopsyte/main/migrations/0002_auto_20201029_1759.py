# Generated by Django 3.1.2 on 2020-10-29 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='image_path',
        ),
        migrations.AddField(
            model_name='game',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]