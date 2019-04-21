from django.shortcuts import render, redirect, reverse

def show_cart(request):
    cart = request.session.get('cart', {})
    items_in_cart = 0
    for item in cart:
        items_in_cart += 1
    
    return render(request, "cart.html", {"items_in_cart": items_in_cart})

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


def remove_item(request, id):
    cart = request.session.get('cart', {})
    cart.pop(id)
    request.session['cart'] = cart
    
    return redirect("show_cart")