# Generated by Django 5.0.1 on 2024-02-03 00:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transcendenceuser',
            old_name='image',
            new_name='pfp',
        ),
        migrations.RemoveField(
            model_name='transcendenceuser',
            name='profile_picture',
        ),
    ]
