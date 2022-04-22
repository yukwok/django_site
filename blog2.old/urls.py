from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-2-home'),
]
