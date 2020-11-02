# Generated by Django 3.1.2 on 2020-10-18 07:23

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fbuser',
            fields=[
                ('fb_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('fb_name', models.CharField(max_length=30)),
                ('fb_email', models.EmailField(max_length=254)),
                ('fb_password', models.CharField(max_length=30)),
                ('fb_dp', models.ImageField(blank=True, null=True, upload_to='users/')),
            ],
        ),
    ]