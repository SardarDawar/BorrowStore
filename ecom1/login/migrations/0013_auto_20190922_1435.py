# Generated by Django 2.2.3 on 2019-09-22 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0012_auto_20190921_0007'),
    ]

    operations = [
        migrations.CreateModel(
            name='temppic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ImageField(null=True, upload_to='')),
            ],
        ),
        migrations.AlterField(
            model_name='infor',
            name='cover',
            field=models.IntegerField(default=3),
        ),
    ]