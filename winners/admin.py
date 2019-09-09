from django.contrib import admin
from .models import Winner

class WinnerAdmin(admin.ModelAdmin):
   list_display = ('username', 'competition', 'first_name', 'last_name', 'win_date', 'winning_ticket_number', 'price_of_ticket')
   list_display_links = ('username', 'competition')
   # list_filter = ('is_active',)
   search_fields = ('competition', 'username', 'first_name', 'last_name')
   list_per_page = 25

admin.site.register(Winner, WinnerAdmin)
