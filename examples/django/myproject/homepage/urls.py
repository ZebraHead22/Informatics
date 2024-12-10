from django.urls import path
from . import views

urlpatterns = [
    path('homepage/', views.home, name='home'),
]
