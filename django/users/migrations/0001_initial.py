# Generated by Django 5.0.1 on 2024-02-02 22:55

import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='TranscendenceUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(max_length=55, unique=True)),
                ('profile_picture', models.CharField(default='default.webp', max_length=100)),
                ('image', models.ImageField(default='default.webp', upload_to='pfp')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('score', models.IntegerField(default=500)),
                ('last_activity', models.DateTimeField(auto_now=True)),
                ('creation_method', models.CharField(choices=[('FT', '42_API'), ('GO', 'Google-Auth'), ('RE', 'Regular')], default='RE', max_length=2)),
                ('friends', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to.', related_name='transcendence_user_groups', to='auth.group')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='transcendence_user_permissions', to='auth.permission')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
