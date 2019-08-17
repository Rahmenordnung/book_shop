from django.conf import settings
from django.db.models import Sum
from django.db import models
from literature.models import Work

class OrderItem(models.Model):
  work = models.ForeignKey(Work, on_delete=models.CASCADE) 
  def __str__(self):
    return self.work.title

class Order(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
  item_checked = models.BooleanField(default=False)
  items = models.ManyToManyField(OrderItem)
  ref_code = models.CharField(max_length=40)
  
  def __str__(self):
    return self.user.username
  
  def get_total(self):
        return self.items.all().aggregate(order_total=Sum('work__price'))['order_total']
  
class money_payment(models.Model):
  order = models.ForeignKey(Order, on_delete=models.CASCADE)
  total_amount = models.FloatField()
  date_paid = models.DateTimeField(auto_now_add=True)
  stripe_charge_id = models.CharField(max_length=100)
  
  def __str__(self):
    return self.stripe_charge_id  