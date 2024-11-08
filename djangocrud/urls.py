"""
URL configuration for djangocrud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Glamrush import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('interfaz/', views.interfaz, name='interfaz'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
    path('add-product/', views.add_product, name='add_product'),  
    path('add-to-cart/<int:product_id>/', views.add_to_cart_view, name='add_to_cart'),  # Ruta para agregar al carrito
    path('view-cart/', views.view_cart_view, name='view_cart'),  # Ruta para ver el carrito
    path('remove-from-cart/<int:product_id>/', views.remove_from_cart_view, name='remove_from_cart'),  # Ruta para eliminar del carrito
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
