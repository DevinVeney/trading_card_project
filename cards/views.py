from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Card, UserCollection
from django.contrib.auth.decorators import login_required
from django_htmx.http import HttpResponseClientRedirect

@login_required
def card_gallery(request):
    cards = Card.objects.all()
    return render(request, 'cards/card_list.html', {'cards': cards})

@login_required
def open_pack(request):
    # Simulate opening a pack with 5 random cards
    import random
    cards = list(Card.objects.all())
    new_cards = random.sample(cards, 5)

    # Add cards to user's collection
    collection, _ = UserCollection.objects.get_or_create(user=request.user)
    for card in new_cards:
        collection.cards.add(card)

    return render(request, 'cards/open_pack.html', {'new_cards': new_cards})
