from django.urls import path
from . import views

urlpatterns = [
    path('', views.card_gallery, name='card_gallery'),
    path('open-pack/', views.open_pack, name='open_pack'),
]
