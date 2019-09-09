from django.contrib.postgres.fields import ArrayField
from django.db import models
from competitions.models import Competition


class Cart(models.Model):
   cart_id = models.CharField(max_length=250, blank=True)
   date_added = models.DateField(auto_now_add=True)

   def __str__(self):
      return self.cart_id

class CartItem(models.Model):
   competition = models.ForeignKey(Competition, on_delete=models.CASCADE)
   cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
   quantity = models.IntegerField()
   ticket_numbers = ArrayField(models.IntegerField())
   active = models.BooleanField(default=True)

   def sub_total(self):
      if self.competition.sale_ticket_price:
         return self.competition.sale_ticket_price * self.quantity
      else:
         return self.competition.price_of_ticket * self.quantity
   
   def __str__(self):
      return self.competition