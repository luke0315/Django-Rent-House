
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse
from .models import Community, House
from .filters import HouseFilter
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

class houseListView(ListView):
    model = House
    template_name = 'home.html'
    

    
class houseCreateView(CreateView):
    model = House
    template_name = 'housenew.html'
    
    fields = ['description' ,'community','bedroom','direction','floor','area','price','phone' ]
 
    def get_success_url(self):
        
        return reverse('home')


# Filter houses
def house_filter(request):
    base_qs = House.objects.all().select_related('community')
    f = HouseFilter(request.GET, queryset=base_qs)
    paginator = Paginator(f.qs, 5)
    page = request.GET.get('page', 1)
    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    is_paginated = True if paginator.num_pages > 1 else False
    context = {'page_obj': page_obj, 'paginator': paginator, 'is_paginated': is_paginated, 'filter': f, }
    print(context)

    return render(request, 'home.html', context)

