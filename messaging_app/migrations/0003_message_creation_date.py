# Generated by Django 3.0.6 on 2020-05-20 14:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messaging_app', '0002_message_unread'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='creation_date',
            field=models.DateField(default=datetime.datetime(2020, 5, 20, 14, 27, 33, 311299)),
            preserve_default=False,
        ),
    ]
