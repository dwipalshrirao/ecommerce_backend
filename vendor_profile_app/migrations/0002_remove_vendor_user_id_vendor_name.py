# Generated by Django 4.1 on 2024-05-01 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor_profile_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendor',
            name='user_id',
        ),
        migrations.AddField(
            model_name='vendor',
            name='name',
            field=models.CharField(default='abc', max_length=100),
            preserve_default=False,
        ),
    ]