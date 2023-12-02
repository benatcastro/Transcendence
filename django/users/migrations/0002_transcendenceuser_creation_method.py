# Generated by Django 4.2.7 on 2023-12-02 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transcendenceuser',
            name='creation_method',
            field=models.CharField(choices=[('FT', '42_API'), ('GO', 'Google-Auth'), ('RE', 'Regular')], default='RE', max_length=2),
        ),
    ]
