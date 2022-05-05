# Generated by Django 4.0.4 on 2022-05-05 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_usermodel_created_at_remove_usermodel_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='usermodel',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
