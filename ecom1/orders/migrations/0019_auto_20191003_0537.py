# Generated by Django 2.2 on 2019-10-03 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0018_auto_20191003_0536'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assset_tracker_activity',
            old_name='staff_name',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='assset_tracker_activity',
            name='location_being_moved_to',
            field=models.TextField(blank=True, default='2019-10-03'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='assset_tracker_activity',
            name='move_date',
            field=models.DateField(blank=True, default='2019-10-03'),
            preserve_default=False,
        ),
    ]
