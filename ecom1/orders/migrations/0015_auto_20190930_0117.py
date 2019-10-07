# Generated by Django 2.2 on 2019-09-29 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0014_auto_20190927_0151'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='location',
            name='locatio',
        ),
        migrations.AddField(
            model_name='location',
            name='location',
            field=models.CharField(default='2019-05-01', max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='assset_tracker_activity',
            name='due_for_pickup',
            field=models.DateField(blank=True, default='2019-05-01'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='staff_contractor_company',
            name='emergency_contact',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='staff_contractor_company',
            name='emergency_phone',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='staff_contractor_company',
            name='fax_number',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='staff_contractor_company',
            name='mobile_phone',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='staff_contractor_company',
            name='work_phone',
            field=models.CharField(max_length=1000),
        ),
    ]
