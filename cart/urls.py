from django.urls import path 
from . import views

app_name='cart'

urlpatterns = [
   path('add/<int:competition_id>', views.add_cart, name='add_cart'),
   path('', views.cart_detail, name='cart_detail'),
   path('remove/<int:competition_id>', views.cart_remove, name='cart_remove'),
   path('full_remove/<int:competition_id>', views.full_remove, name='full_remove'),
   path('plus_icon/<int:competition_id>', views.plus_icon, name='plus_icon'),
   path('remove_from_ticket_array/<int:competition_id>', views.remove_from_ticket_array, name='remove_from_ticket_array'),
]