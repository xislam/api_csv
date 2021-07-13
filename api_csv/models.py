from django.db import models
from django.db.models import Sum


class UserQuerySet(models.QuerySet):

    def top_buyers(self):
        top_buyers = User.objects.annotate(total_sum=Sum('transaction__total')).order_by('-total_sum')
        return top_buyers


class User(models.Model):
    objects = UserQuerySet.as_manager()
    username = models.CharField(max_length=35)


class Gem(models.Model):
    text = models.CharField(max_length=35)


class Transaction(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transaction')
    item = models.ForeignKey(Gem, on_delete=models.CASCADE, related_name='transaction')
    total = models.IntegerField(verbose_name="total")
    quantity = models.IntegerField(verbose_name="quantity")
    date = models.DateTimeField(verbose_name="date")

    def __str__(self):
        return self.customer
