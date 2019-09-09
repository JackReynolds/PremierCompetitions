from django.shortcuts import render
from django.http import HttpResponse
from competitions.models import Competition
from winners.models import Winner
from django.contrib.auth.models import User

def index(request):
   competitions = Competition.objects.order_by('-list_date').filter(is_active=True)[:3]
   winners = Winner.objects.all()
   context = {
      'competitions': competitions,
      'winners': winners
   }
   return render(request, 'pages/index.html', context)

def about(request):
   return render(request, 'pages/about.html')

def cookiePolicy(request):
   return render(request, 'pages/cookiePolicy.html')

def privacyPolicy(request):
   return render(request, 'pages/privacyPolicy.html')

def termsAndConditions(request):
   return render(request, 'pages/termsAndConditions.html')

def FAQ(request):
   return render(request, 'pages/FAQ.html')

def cart(request):
   return render(request, 'cart/cart.html')
