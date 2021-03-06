# Generated by Django 3.1.5 on 2021-04-15 21:29

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0003_logentry_add_action_flag_choices'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('django_twilio', '0001_initial'),
        ('App_1', '0003_auto_20210416_0248'),
    ]

    operations = [
        migrations.CreateModel(
            name='Officers',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.user')),
            ],
            options={
                'db_table': 'Officers',
            },
            bases=('auth.user',),
            managers=[
                ('man_objects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.RenameModel(
            old_name='CustomUserModel',
            new_name='Moderator',
        ),
        migrations.AlterField(
            model_name='licenseregistration',
            name='doi',
            field=models.DateField(default=datetime.datetime(2021, 4, 16, 2, 59, 42, 587457)),
        ),
        migrations.AlterField(
            model_name='rcregister',
            name='reg_date',
            field=models.DateField(default=datetime.datetime(2021, 4, 16, 2, 59, 42, 587457)),
        ),
        migrations.AlterField(
            model_name='vechilefine',
            name='offence_on',
            field=models.DateField(default=datetime.datetime(2021, 4, 16, 2, 59, 42, 587457)),
        ),
        migrations.AlterField(
            model_name='vechilefine',
            name='paid_upto',
            field=models.DateField(default=datetime.datetime(2021, 6, 16, 2, 59, 42, 587457)),
        ),
    ]
