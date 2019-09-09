# Generated by Django 2.2.3 on 2019-09-04 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0011_competition_sale_ticket_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competition',
            name='sale_ticket_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
