from django.urls import path 
from . import views

urlpatterns = [
   path('', views.index, name='index'),
   path('about', views.about, name='about'),
   path('termsAndConditions', views.termsAndConditions, name='termsAndConditions'),
   path('cookiePolicy', views.cookiePolicy, name='cookiePolicy'),
   path('privacyPolicy', views.privacyPolicy, name='privacyPolicy'),
   path('FAQ', views.FAQ, name='FAQ'),
   path('cart', views.cart, name='cart')
]