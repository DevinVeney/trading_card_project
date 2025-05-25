from django.shortcuts import render, get_object_or_404
from .models import Card, UserCollection
from django.contrib.auth.decorators import login_required
from django.db.models import Q

@login_required
def card_gallery(request):
    cards = Card.objects.all()
    return render(request, 'cards/card_list.html', {'cards': cards})

@login_required
def search_cards(request):
    query = request.GET.get('q', '').strip()
    
    if query:
        # Search in card name, description, and rarity
        cards = Card.objects.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(rarity__icontains=query)
        ).distinct()
    else:
        # If no query, return all cards
        cards = Card.objects.all()
    
    # Return only the card grid partial template for HTMX
    return render(request, 'cards/partials/card_grid.html', {'cards': cards})

def homepage(request):
    # Will point to my homepage template
    return render(request, 'cards/homepage.html')

@login_required
def card_detail(request, card_id):
    card = get_object_or_404(Card, id=card_id)
    
    # Get user's collection to check if they own this card
    try:
        collection = UserCollection.objects.get(user=request.user)
        user_owns_card = collection.cards.filter(id=card_id).exists()
    except UserCollection.DoesNotExist:
        user_owns_card = False
    
    context = {
        'card': card,
        'user_owns_card': user_owns_card,
    }
    return render(request, 'cards/card_detail.html', context)