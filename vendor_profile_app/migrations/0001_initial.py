# Generated by Django 4.1 on 2024-05-01 13:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('modification_date', models.DateTimeField(auto_now=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('vendor_id', models.AutoField(db_column='vendor_id', primary_key=True, serialize=False)),
                ('contact_details', models.TextField()),
                ('address', models.TextField()),
                ('vendor_code', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('on_time_delivery_rate', models.FloatField(null=True)),
                ('quality_rating_avg', models.FloatField(null=True)),
                ('average_response_time', models.FloatField(null=True)),
                ('fulfillment_rate', models.FloatField(null=True)),
                ('user_id', models.OneToOneField(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]