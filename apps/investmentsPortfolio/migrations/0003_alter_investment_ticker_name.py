# Generated by Django 4.2.16 on 2024-11-21 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investmentsPortfolio', '0002_investment_ticker_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investment',
            name='ticker_name',
            field=models.CharField(max_length=10),
        ),
    ]
