# Generated by Django 2.2.3 on 2019-07-25 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0005_competition_tickets_remaining'),
    ]

    operations = [
        migrations.AddField(
            model_name='competition',
            name='slug',
            field=models.SlugField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
