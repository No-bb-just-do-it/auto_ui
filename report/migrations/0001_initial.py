# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-18 03:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precondition', models.CharField(default=None, max_length=255, verbose_name='\u524d\u7f6e\u6761\u4ef6')),
                ('case_name', models.CharField(default=None, max_length=128, verbose_name='case\u540d\u79f0')),
                ('check_step', models.CharField(default=None, max_length=128, verbose_name='\u68c0\u67e5\u6b65\u9aa4')),
                ('title', models.CharField(default=None, max_length=64, verbose_name='\u7528\u4f8b\u6807\u9898')),
                ('step', models.TextField(default=None, max_length=2048, verbose_name='\u6d4b\u8bd5\u6b65\u9aa4')),
                ('phone_name', models.CharField(default=None, max_length=64, verbose_name='\u673a\u578b')),
                ('result', models.ImageField(default=0, upload_to=b'', verbose_name='\u6d4b\u8bd5\u7ed3\u679c')),
                ('msg', models.TextField(default=None, max_length=1024, verbose_name='\u5931\u8d25\u539f\u56e0')),
                ('case_id', models.CharField(default=None, max_length=64, verbose_name='case_id')),
                ('report_uuid', models.CharField(default=None, max_length=256, verbose_name='\u6bcf\u6b21\u8fd0\u884c\u552f\u4e00md5\u6807\u8bc6')),
                ('report_create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('report_update_time', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
            ],
        ),
    ]
