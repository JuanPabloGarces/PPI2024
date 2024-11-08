from django.shortcuts import get_object_or_404, redirect, render
from .models import Glamrush

# Agregar un producto al carrito
def add_to_cart(request, product_id):
    product = get_object_or_404(Glamrush, pk=product_id)
    # Lógica para agregar el producto al carrito
    if 'cart' not in request.session:
        request.session['cart'] = []
    request.session['cart'].append(product.id)
    request.session.modified = True
    return redirect('view_cart')  # Redirigir a la vista del carrito

# Ver el carrito
def view_cart(request):
    cart_ids = request.session.get('cart', [])
    products = Glamrush.objects.filter(id__in=cart_ids)
    return render(request, 'cart.html', {'products': products})

# Eliminar un producto del carrito
def remove_from_cart(request, product_id):
    cart = request.session.get('cart', [])
    if product_id in cart:
        cart.remove(product_id)
        request.session.modified = True
    return redirect('view_cart')  # Redirigir a la vista del carrito
