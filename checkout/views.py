from django.shortcuts import render, get_object_or_404, redirect, render
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import PaymentForm, OrderForm
from .models import OrderLineItem
import stripe
from django.utils import timezone
from features.models import Features
from features import views

stripe.api_key = settings.STRIPE_SECRET

# Price per vote is $0.10. Votes are sold in 1000's 

VOTE_PRICE = 0.1
VOTES_PER_INCREMENT = 1000



@login_required()
def checkout(request):
    cart_page = "active"
    if request.method == "POST":
        order_form = OrderForm(request.POST)
        payment_form = PaymentForm(request.POST)

        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()

            cart = request.session.get('cart', {})
            total = 0
            # Calculate the total charge
            for id, quantity in cart.items():
                feature = get_object_or_404(Features, pk=id)
                total += quantity * VOTE_PRICE * VOTES_PER_INCREMENT
                order_line_item = OrderLineItem(
                    order = order,
                    feature = feature,
                    quantity = quantity
                )
                order_line_item.save()
            # Attempt to charge the user
            try:
                customer = stripe.Charge.create(
                    amount = int(total * 100),
                    currency = "USD",
                    description = request.user.email,
                    card = payment_form.cleaned_data['stripe_id'],                    
                )
            except stripe.error.CardError:
                messages.error(request, "Your credit card was declined")
            
            # If payment succeeds, add the purchased votes to the feature's total votes
            if customer.paid:
                messages.success(request, "You have successfully paid. Thank you for purchasing upvotes!")

                #Add the Votes
                for id, quantity in cart.items():
                    feature = get_object_or_404(Features, pk=id)
                    votes = quantity * 1000
                    feature.upvotes += votes
                    feature.save()

                #Continue to clear cart and move on                 
                request.session['cart'] = {}
                return redirect('payment_success')
            else:
                messages.error(request, "Error with transaction")

        else:
            print(payment_form.errors)
            messages.error(request, "Error in taking payment from specified card")

    else:
        payment_form = PaymentForm()
        order_form = OrderForm()

    return render(request, "checkout.html", {'order_form': order_form, 'payment_form': payment_form, 'publishable': settings.STRIPE_PUBLISHABLE, 'cart_page': cart_page})

# Once payment is complete, direct user to a page to acknowledge it
def payment_success(request):
    return render(request, "success.html")
