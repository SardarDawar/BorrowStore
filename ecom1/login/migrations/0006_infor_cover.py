# Generated by Django 2.2.3 on 2019-09-14 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_privacy_policy_and_terms_of_service'),
    ]

    operations = [
        migrations.AddField(
            model_name='infor',
            name='cover',
            field=models.IntegerField(default=10),
        ),
    ]
