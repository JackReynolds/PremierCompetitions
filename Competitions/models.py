from django.contrib.postgres.fields import ArrayField
from django.db import models
from datetime import datetime
from django.urls import reverse

class Competition(models.Model):
   title = models.CharField(max_length=200)
   slug = models.SlugField(max_length=200, unique=True)  
   number_of_tickets = models.IntegerField()
   ticket_array = ArrayField(models.IntegerField())
   tickets_sold = models.IntegerField()
   price_of_ticket = models.DecimalField(max_digits=10, decimal_places=2)
   sale_ticket_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
   description = models.TextField()
   question = models.CharField(max_length=200)
   wrong_answer1 = models.CharField(max_length=200)
   wrong_answer2 = models.CharField(max_length=200)
   right_answer = models.CharField(max_length=200)
   video_url = models.CharField(max_length=1000, blank=True)
   photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
   photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
   photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
   photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
   photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
   photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
   is_active = models.BooleanField(default=True)
   list_date = models.DateField(default=datetime.now, blank=True)
   end_date = models.DateField()
   def __str__(self):
      return self.title

   def get_url(self):
      return reverse('competition', args=[self.slug])
   
   @property
   def percentage_tickets_sold(self):
      return (100 -(100*((self.number_of_tickets - self.tickets_sold)/self.number_of_tickets)))

   @property
   def remaining_tickets(self):
      return self.number_of_tickets - self.tickets_sold

   

