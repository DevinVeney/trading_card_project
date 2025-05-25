from django.urls import path
from . import views

urlpatterns = [
    path("", views.card_gallery, name="card_gallery"),
    path("/cards/<int:card_id>", views.card_detail, name="card_detail"),
    path("search/", views.search_cards, name="search_cards"),
]
