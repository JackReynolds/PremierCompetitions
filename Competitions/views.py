from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Competition


def index(request):
   competitions = Competition.objects.order_by('-list_date').filter(is_active=True)

   paginator = Paginator(competitions, 3)
   page = request.GET.get('page')
   paged_competitions = paginator.get_page(page)

   context = {
      'competitions': paged_competitions
   }  
   return render(request, 'competitions/competitions.html', context)

def competition(request, c_slug):
   competition = get_object_or_404(Competition, slug=c_slug)

   context = {
      'competition': competition
   }

   return render(request, 'competitions/competition.html', context)
