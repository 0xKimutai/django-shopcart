from django.shortcuts import render, redirect, get_object_or_404
from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = request.session.get('cart', {})
    cart[str(product_id)] = cart.get(str(product_id), 0) + 1
    request.session['cart'] = cart
    return redirect('product_list')

def cart_view(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total = 0

    for key, quantity in cart.items():
        if "_" in key:
            name, price = key.rsplit('_', 1)
            price = float(price)
            subtotal = price * quantity
            cart_items.append({
                'product': {'name': name, 'price': price},
                'quantity': quantity,
                'subtotal': subtotal,
                'custom': True,
                'key': key
            })
        else:
            try:
                product = Product.objects.get(id=key)
                subtotal = product.price * quantity
                cart_items.append({
                    'product': product,
                    'quantity': quantity,
                    'subtotal': subtotal,
                    'custom': False,
                    'key': product.id
                })
                total += subtotal
            except Product.DoesNotExist:
                continue

        total += subtotal

    return render(request, 'store/cart.html', {'cart_items': cart_items, 'total': total})
def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    cart[product_id] = cart.get(product_id, 0) + 1 #Increment quantity
    request.session['cart'] = cart# save back to session
    return redirect('product_list') #Redirect back to product page
def add_to_cart(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = float(request.POST.get('price'))
        quantity = int(request.POST.get('quantity', 1))

        cart = request.session.get('cart', {})

        #create a fake ID for custom entries
        key = f"{name}_{price}"
        if key in cart:
            cart[key] += quantity
        else:
            cart[key] = quantity

        request.session['cart'] = cart
        request.session.modified = True

    return redirect('product_list')
def remove_from_cart(request, key):
    cart = request.session.get('cart', {})
    if key in cart:
        del cart[key]
        request.session['cart'] = cart
        request.session.modified = True
    return redirect('cart_view')
