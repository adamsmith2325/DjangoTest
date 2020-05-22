# Generated by Django 3.0.6 on 2020-05-20 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AgencyProfiles', '0003_auto_20200520_1604'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agent',
            name='content',
        ),
        migrations.AddField(
            model_name='agent',
            name='additionalInfo',
            field=models.TextField(default='null'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='agent',
            name='agencyName',
            field=models.TextField(default='null'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='agent',
            name='agriculture',
            field=models.BinaryField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='agent',
            name='bizEmail',
            field=models.TextField(default='null'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='agent',
            name='city',
            field=models.TextField(default='null'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='agent',
            name='construction',
            field=models.BinaryField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='agent',
            name='cyber',
            field=models.BinaryField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='agent',
            name='excess',
            field=models.BinaryField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='agent',
            name='firstName',
            field=models.TextField(default='null'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='agent',
            name='large',
            field=models.BinaryField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='agent',
            name='lastName',
            field=models.TextField(default='null'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='agent',
            name='managementLiab',
            field=models.BinaryField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='agent',
            name='manufacturing',
            field=models.BinaryField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='agent',
            name='middleMarket',
            field=models.BinaryField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='agent',
            name='phone',
            field=models.TextField(default='null'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='agent',
            name='postal',
            field=models.TextField(default='null'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='agent',
            name='proLiab',
            field=models.BinaryField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='agent',
            name='product',
            field=models.BinaryField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='agent',
            name='prop',
            field=models.BinaryField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='agent',
            name='publicEntity',
            field=models.BinaryField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='agent',
            name='realEstate',
            field=models.BinaryField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='agent',
            name='retail',
            field=models.BinaryField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='agent',
            name='smb',
            field=models.BinaryField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='agent',
            name='state',
            field=models.TextField(default='null'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='agent',
            name='streetAddress1',
            field=models.TextField(default='null'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='agent',
            name='streetAddress2',
            field=models.TextField(default='null'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='agent',
            name='tech',
            field=models.BinaryField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='agent',
            name='transportation',
            field=models.BinaryField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='agent',
            name='trucking',
            field=models.BinaryField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='agent',
            name='wcom',
            field=models.BinaryField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='agent',
            name='wholesale',
            field=models.BinaryField(default=0),
            preserve_default=False,
        ),
    ]
