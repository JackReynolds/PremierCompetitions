from django.db import models
from competitions.models import Competition
from datetime import datetime

class Winner(models.Model):
   competition = models.ForeignKey(Competition, on_delete=models.DO_NOTHING)
   username = models.CharField(max_length=50)
   number_of_tickets = models.IntegerField()
   price_of_ticket = models.DecimalField(max_digits=10, decimal_places=2)
   first_name = models.CharField(max_length=50)
   last_name = models.CharField(max_length=50)
   winning_ticket_number = models.IntegerField()
   win_date = models.DateField(default=datetime.now, blank=True)
   photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
   def __str__(self):
      return f"{self.first_name} {self.last_name} - {self.competition} - Winning Ticket Number: {self.winning_ticket_number}"

