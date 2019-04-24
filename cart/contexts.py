from django.shortcuts import get_object_or_404
from features.models import Features

# Context file for the cart contents
# Users select an amount in thousands to purchase. The unit price (per vote) is $0.1 which means 1000 votes will cost $100
# Selected vote amount is multiplied by 1000 then by the unit price in order to get the total cost per item (rounded_total)
# Combined cost of all items in cart is the combined_total

def cart_contents(request):
    cart = request.session.get('cart', {})
    
    combined_total = 0
    cart_items = []
    vote_count = 0
    price_per_vote = 0.10
    print(cart.items())
    for id, quantity in cart.items():
        total = 0
        feature = get_object_or_404(Features, pk=id)
        total += quantity * 1000 * price_per_vote
        votes_multiplied = quantity * 1000
        vote_count += quantity
        rounded_total = int(total)
        combined_total += rounded_total
        print(id, rounded_total, votes_multiplied)
        cart_items.append({'id': id, 'votes_multiplied': votes_multiplied, 'rounded_total': rounded_total, 'feature': feature})

    return {'cart_items': cart_items, 'combined_total': combined_total}