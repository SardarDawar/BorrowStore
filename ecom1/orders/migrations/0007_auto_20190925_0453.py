# Generated by Django 2.2.5 on 2019-09-24 23:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.assset_tracker_activity'),
        ),
    ]