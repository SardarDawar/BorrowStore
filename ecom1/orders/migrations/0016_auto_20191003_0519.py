# Generated by Django 2.2 on 2019-10-03 00:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0015_auto_20190930_0117'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staff_contractor_company',
            old_name='user',
            new_name='staff_name',
        ),
    ]
