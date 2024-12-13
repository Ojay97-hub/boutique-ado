from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51QVXn0FZfI4sG0CkYDEojavmVZHMeLv9a0AoGLqEMya0o7Dob6DKxQifltbSfFoMspvRxQnMjrg5A7IbkCYP3F420004WNosR7', 
    }

    return render(request, template, context)