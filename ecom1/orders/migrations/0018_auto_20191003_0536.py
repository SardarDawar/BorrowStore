# Generated by Django 2.2 on 2019-10-03 00:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0017_auto_20191003_0534'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staff_contractor_company',
            old_name='staff_name',
            new_name='user',
        ),
    ]