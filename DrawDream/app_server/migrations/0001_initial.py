# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-03 13:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('acco_id', models.AutoField(primary_key=True, serialize=False)),
                ('acco_num', models.CharField(max_length=32, unique=True)),
                ('acco_pwd', models.CharField(max_length=18)),
                ('acco_create_date', models.DateField(auto_now_add=True)),
                ('acco_modify_date', models.DateField(null=True)),
                ('acco_login_date', models.DateField(null=True)),
                ('acco_count', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'account',
            },
        ),
        migrations.CreateModel(
            name='CommentReplay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('core_content', models.CharField(max_length=512)),
                ('core_date', models.DateField(auto_now_add=True)),
            ],
            options={
                'db_table': 'comment_reply',
            },
        ),
        migrations.CreateModel(
            name='NewsClassify',
            fields=[
                ('necl_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('necl_name', models.CharField(max_length=64, unique=True)),
                ('necl_create_date', models.DateField(auto_now_add=True)),
            ],
            options={
                'db_table': 'news_classify',
            },
        ),
        migrations.CreateModel(
            name='NewsDetail',
            fields=[
                ('nede_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nede_create_date', models.DateField(auto_now_add=True)),
                ('nede_title', models.CharField(max_length=128)),
                ('nede_author', models.CharField(default='佚名', max_length=64)),
                ('nede_time', models.CharField(max_length=32, null=True)),
                ('nede_content', models.TextField()),
                ('nesu_count', models.IntegerField(default=0)),
                ('nesu_like', models.IntegerField(default=0)),
                ('nede_classify', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_server.NewsClassify', to_field='necl_name')),
            ],
            options={
                'db_table': 'news_detail',
            },
        ),
        migrations.CreateModel(
            name='UserCollect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usco_create_date', models.DateField(auto_now_add=True)),
                ('usco_acco_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_server.NewsDetail')),
            ],
            options={
                'db_table': 'user_collect',
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('usin_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='app_server.Account')),
                ('usin_name', models.CharField(default='漫画小迷弟', max_length=32)),
                ('usin_sex', models.BooleanField()),
                ('usin_phone', models.CharField(max_length=20, null=True, unique=True)),
                ('usin_email', models.EmailField(max_length=254)),
                ('usin_sign', models.CharField(default='这个人很懒，什么也没留下', max_length=256)),
            ],
            options={
                'db_table': 'user_info',
            },
        ),
        migrations.AddField(
            model_name='commentreplay',
            name='core_acco_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_server.Account'),
        ),
        migrations.AddField(
            model_name='commentreplay',
            name='core_nede_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_server.NewsDetail'),
        ),
        migrations.AlterUniqueTogether(
            name='commentreplay',
            unique_together=set([('core_acco_id', 'core_nede_id')]),
        ),
    ]
