# Generated by Django 2.1.13 on 2019-10-07 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20190930_0115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date_remove',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
