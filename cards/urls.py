from django.urls import path
from . import views

urlpatterns = [
    path('', views.card_gallery, name='card_gallery'),
    
]
