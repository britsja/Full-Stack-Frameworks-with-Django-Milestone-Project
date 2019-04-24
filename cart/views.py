from django.shortcuts import render, redirect, reverse

# View for cart and returns total items in cart
def show_cart(request):
    cart_page = "active"
    cart = request.session.get('cart', {})
    items_in_cart = 0
    for item in cart:
        items_in_cart += 1
    
    return render(request, "cart.html", {"items_in_cart": items_in_cart, 'cart_page': cart_page})

# Add item to cart. If same item was already in cart, remove it and add new quantity of item. If no items, catch the error when using .pop
def add_cart(request, id):
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    try:
        cart.pop(id)
    except:
        pass
    
    request.session['cart'] = cart
    cart[id] = cart.get(id, quantity)

    request.session['cart'] = cart
    
    return redirect("show_cart")

#  Remove item and redirect back to cart page
def remove_item(request, id):
    cart = request.session.get('cart', {})
    cart.pop(id)
    request.session['cart'] = cart
    
    return redirect("show_cart")