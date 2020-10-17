from django.urls import path
from website import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('date', views.date, name='date'),
    path('about', views.about, name='about'),
    ]