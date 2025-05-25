from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Card
from django_htmx.http import HttpResponseClientRedirect
from django.db.models import Q


def card_gallery(request):
    cards = Card.objects.all()
    print(cards)
    return render(request, "cards/card_list.html", {"cards": cards})


def card_detail(request, card_id):
    card = get_object_or_404(Card, id=card_id)
    return render(request, "cards/card_detail.html", {"card": card})


def search_cards(request):
    query = request.GET.get("q", "").strip()
    print(query)
    if query:
        # Search in card name, description, and rarity
        cards = Card.objects.filter(
            Q(name__icontains=query)
            | Q(description__icontains=query)
            | Q(rarity__icontains=query)
        ).distinct()
    else:
        # If no query, return all cards
        cards = Card.objects.all()

    # Return only the card grid partial template for HTMX
    return render(request, "cards/partials/search_results.html", {"cards": cards})
