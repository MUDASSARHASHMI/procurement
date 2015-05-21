# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('consumers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConsumerAddress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('street_address', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=150)),
                ('zipcode', models.IntegerField(max_length=5, null=True, blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Addresses',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ConsumerCompany',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=120)),
                ('about', models.CharField(max_length=1500, null=True, blank=True)),
                ('company_type', models.CharField(help_text=b'public or private?', max_length=120)),
                ('gst_number', models.CharField(max_length=120)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'companies',
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='address',
            name='company',
        ),
        migrations.RemoveField(
            model_name='address',
            name='user',
        ),
        migrations.DeleteModel(
            name='Address',
        ),
        migrations.RemoveField(
            model_name='company',
            name='user',
        ),
        migrations.DeleteModel(
            name='Company',
        ),
        migrations.AddField(
            model_name='consumeraddress',
            name='company',
            field=models.ForeignKey(to='consumers.ConsumerCompany'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='consumeraddress',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
