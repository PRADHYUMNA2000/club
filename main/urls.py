from django.urls import path
from main import views

urlpatterns = [
    path('',views.index, name = 'index'),
    path('register/',views.register, name = 'register'),
    path('team/',views.team , name = 'team'),
    path('events/',views.events,name="events")
]