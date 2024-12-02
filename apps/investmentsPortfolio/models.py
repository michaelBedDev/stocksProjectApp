from django.db import models


# Create your models here.
class Investment(models.Model):
    id = models.AutoField(primary_key=True)
    ticker_name = models.CharField(max_length=10)
    stocks_amount = models.DecimalField(max_digits=10, decimal_places=2)
    price_at_purchase = models.DecimalField(max_digits=10, decimal_places=2)
    total_investment = models.DecimalField(max_digits=10, decimal_places=2)

    @property
    def total_investment(self):
        return self.stocks_amount * self.price_at_purchase

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    sold = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.ticker_name}"
