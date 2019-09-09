from django.urls import path 
from . import views

urlpatterns = [
   path('', views.index, name='competitions'),
   path('<slug:c_slug>/', views.competition, name='competition'),
]