# Generated by Django 4.2.16 on 2024-11-22 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('investmentsPortfolio', '0003_alter_investment_ticker_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='investment',
            name='total_investment',
        ),
    ]
