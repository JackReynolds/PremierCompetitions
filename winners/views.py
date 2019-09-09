from django.shortcuts import render
from .models import Winner
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

def index(request):
   winners = Winner.objects.all()
   paginator = Paginator(winners, 6)
   page = request.GET.get('page')
   paged_winners = paginator.get_page(page)

   context = {
      'winners': paged_winners
   }
   return render(request, 'winners/winners.html', context)
