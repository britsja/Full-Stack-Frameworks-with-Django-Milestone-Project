from django.shortcuts import get_object_or_404
from features.models import Features

def cart_contents(request):
    cart = request.session.get('cart', {})

    cart_items = []
    total = 0
    vote_count = 0
    price_per_vote = 0.1
    for id, quantity in cart.items():
        feature = get_object_or_404(Features, pk=id)
        total += quantity * price_per_vote
        vote_count += quantity
        cart_items.append({'id': id, 'quantity': quantity, 'product': product})

    return {'cart_items': cart_items, 'total': total}