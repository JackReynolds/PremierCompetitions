# Generated by Django 2.2.3 on 2019-07-19 11:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0003_auto_20190718_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competition',
            name='list_date',
            field=models.DateField(blank=True, default=datetime.datetime.now),
        ),
    ]
