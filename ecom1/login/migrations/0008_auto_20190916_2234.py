# Generated by Django 2.2.3 on 2019-09-16 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_auto_20190916_2122'),
    ]

    operations = [
        migrations.AddField(
            model_name='infor',
            name='cover_check',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='infor',
            name='cover_img',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='infor',
            name='profile_check',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='infor',
            name='profile_pic',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='infor',
            name='cover',
            field=models.IntegerField(default=4),
        ),
    ]
