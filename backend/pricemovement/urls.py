from django.urls import path
from . import views
from . views import get_date, get_price

urlpatterns = [
    path('', views.get_date, name='get_date'),
    path('get_price/', views.get_price, name='get_price'),
    path('get_date/', views.get_date, name='get_date'),
    path('bokehchart/', views.get_bokehchart, name='bokehchart'),
]
