from django.urls import path,include
from .views import houseListView,houseCreateView
from . import views

urlpatterns = [
    path('', houseListView.as_view(), name='home'),
    path('house/new/', houseCreateView.as_view(), name='housenew'),
    path('users/', include('users.urls')),
    path('q', views.house_filter, name='house_filter'),
    ]