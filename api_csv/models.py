from django.db import models


class Transaction(models.Model):
    customer = models.CharField(max_length=50, verbose_name="customer")
    item = models.CharField(max_length=150, verbose_name="item")
    total = models.IntegerField(verbose_name="total")
    quantity = models.IntegerField(verbose_name="quantity")
    date = models.DateTimeField(verbose_name="date")

    def __str__(self):
        return self.customer


