# Generated by Django 3.0.6 on 2020-05-20 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AgencyProfiles', '0002_auto_20200520_1556'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agent',
            name='additionalInfo',
        ),
        migrations.RemoveField(
            model_name='agent',
            name='agencyName',
        ),
        migrations.RemoveField(
            model_name='agent',
            name='agriculture',
        ),
        migrations.RemoveField(
            model_name='agent',
            name='bizEmail',
        ),
        migrations.RemoveField(
            model_name='agent',
            name='city',
        ),
        migrations.RemoveField(
            model_name='agent',
            name='construction',
        ),
        migrations.RemoveField(
            model_name='agent',
            name='cyber',
        ),
        migrations.RemoveField(
            model_name='agent',
            name='excess',
        ),
        migrations.RemoveField(
            model_name='agent',
            name='firstName',
        ),
        migrations.RemoveField(
            model_name='agent',
            name='large',
        ),
        migrations.RemoveField(
            model_name='agent',
            name='lastName',
        ),
        migrations.RemoveField(
            model_name='agent',
            name='managementLiab',
        ),
        migrations.RemoveField(
            model_name='agent',
            name='manufacturing',
        ),
        migrations.RemoveField(
            model_name='agent',
            name='middleMarket',
        ),
        migrations.RemoveField(
            model_name='agent',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='agent',
            name='postal',
        ),
        migrations.RemoveField(
            model_name='agent',
            name='proLiab',
        ),
        migrations.RemoveField(
            model_name='agent',
            name='product',
        ),
        migrations.RemoveField(
            model_name='agent',
            name='prop',
        ),
        migrations.RemoveField(
            model_name='agent',
            name='publicEntity',
        ),
        migrations.RemoveField(
            model_name='agent',
            name='realEstate',
        ),
        migrations.RemoveField(
            model_name='agent',
            name='retail',
        ),
        migrations.RemoveField(
            model_name='agent',
            name='smb',
        ),
        migrations.RemoveField(
            model_name='agent',
            name='state',
        ),
        migrations.RemoveField(
            model_name='agent',
            name='streetAddress1',
        ),
        migrations.RemoveField(
            model_name='agent',
            name='streetAddress2',
        ),
        migrations.RemoveField(
            model_name='agent',
            name='tech',
        ),
        migrations.RemoveField(
            model_name='agent',
            name='transportation',
        ),
        migrations.RemoveField(
            model_name='agent',
            name='trucking',
        ),
        migrations.RemoveField(
            model_name='agent',
            name='wcom',
        ),
        migrations.RemoveField(
            model_name='agent',
            name='wholesale',
        ),
        migrations.AddField(
            model_name='agent',
            name='content',
            field=models.TextField(default='null'),
            preserve_default=False,
        ),
    ]
