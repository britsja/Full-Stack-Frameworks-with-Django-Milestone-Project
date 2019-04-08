from django.shortcuts import get_object_or_404
from features.models import Features

def cart_contents(request):
    cart = request.session.get('cart', {})

    cart_items = []
    total = 0
    vote_count = 0
    price_per_vote = 0.10
    for id, quantity in cart.items():
        feature = get_object_or_404(Features, pk=id)
        total += quantity * 1000 * price_per_vote
        votes_multiplied = quantity * 1000
        vote_count += quantity
        rounded_total = int(total)
        cart_items.append({'id': id, 'votes_multiplied': votes_multiplied, 'rounded_total': rounded_total, 'feature': feature})

    return {'cart_items': cart_items, 'total': total}