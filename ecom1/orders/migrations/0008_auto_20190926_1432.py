# Generated by Django 2.2.3 on 2019-09-26 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_auto_20190925_0453'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='quantity',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
