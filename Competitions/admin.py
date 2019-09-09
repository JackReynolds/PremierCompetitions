from django.contrib import admin
from .models import Competition

class CompetitionAdmin(admin.ModelAdmin):
   list_display = ('id', 'title', 'slug', 'is_active', 'list_date', 'number_of_tickets', 'tickets_sold', 'price_of_ticket', 'sale_ticket_price')
   prepopulated_fields = {'slug':('title',)}
   list_display_links = ('id', 'title')
   # list_filter = ('is_active',)
   list_editable = ('is_active',)
   search_fields = ('title', 'description')
   list_per_page = 25

admin.site.register(Competition, CompetitionAdmin)
