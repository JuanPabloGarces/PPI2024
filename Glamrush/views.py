from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import user_passes_test
from .forms import GlamrushForm
from .models import Glamrush

# Vista de inicio
def home(request):
    productos = Glamrush.objects.all()
    return render(request, 'interfaz.html', {'productos': productos})

# Vista de registro de usuario
def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm()
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'],
                                                password=request.POST['password2'])
                user.save()
                login(request, user)
                return redirect('interfaz')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm(),
                    "error": 'Usuario ya existe'
                })
        return render(request, 'signup.html', {
            'form': UserCreationForm(),
            "error": 'Contraseñas no coinciden'
        })

# Vista de interfaz de productos
def interfaz(request):
    productos = Glamrush.objects.all()
    if not productos:
        print("No hay productos en la base de datos.")
    return render(request, 'interfaz.html', {'productos': productos})

# Vista de cierre de sesión
def signout(request):
    logout(request)
    return redirect('home')

# Vista de inicio de sesión
def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm()
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm(),
                'error': 'Usuario o contraseña es incorrecta'
            })
        else:
            login(request, user)
            return redirect('interfaz')

# Nueva función para agregar productos
def is_master(user):
    return user.username == 'juanpablogarces'

@user_passes_test(is_master)
def add_product(request):
    if request.method == 'POST':
        form = GlamrushForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('interfaz')
    else:
        form = GlamrushForm()
    return render(request, 'add_product.html', {'form': form})

# Funciones para el carrito de compras
def add_to_cart_view(request, product_id):
    product = get_object_or_404(Glamrush, pk=product_id)
    if 'cart' not in request.session:
        request.session['cart'] = []
    request.session['cart'].append(product.id)
    request.session.modified = True
    print(f"Carrito actualizado: {request.session['cart']}")  # Para depuración
    return redirect('view_cart')

def view_cart_view(request):
    cart_ids = request.session.get('cart', [])
    products = Glamrush.objects.filter(id__in=cart_ids)
    print(f"Productos en el carrito: {list(products.values_list('id', flat=True))}")  # Para depuración
    return render(request, 'cart.html', {'products': products})

def remove_from_cart_view(request, product_id):
    cart = request.session.get('cart', [])
    if product_id in cart:
        cart.remove(product_id)
        request.session.modified = True
    return redirect('view_cart')
