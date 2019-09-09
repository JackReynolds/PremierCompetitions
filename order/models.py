from django.db import models

# Create your models here.
# class Order(models.Model):
#    token = models.CharField(max_length=250, blank=True)
#    total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="EUR Order Total")
#    email_address = models.EmailField(max_length=250, blank=True, verbose_name="Email Address")
#    created = models.DateTimeField(auto_now_add=True)
#    billing_name = models.CharField(max_length=250, blank=True)
#    billing_address1 = models.CharField(max_length=250, blank=True)
#    billing_postcode = models.CharField(max_length=10, blank=True)
#    billing_country = models.CharField(max_length=200, blank=True)

#    class Meta:
#       db_table = 'Order'
#       ordering = ['-created']

#    def __str__(self):
#       return str(self.id)

# class OrderItem(models.Model):
#    competition = models.CharField(max_length=250)
#    quantity = models.CharField(max_length=250)
#    ticket_numbers = ArrayField(models.IntegerField())
#    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="EUR Price")
#    order = models.ForeignKey(Order, on_delete=models.CASCADE)

#    class Meta:
#       db_table = 'OrderItem'

#    def sub_total(self):
#       return self.quantity * self.price
   
#    def __str__(self):
#       return self.competition