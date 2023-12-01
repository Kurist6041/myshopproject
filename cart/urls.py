from django.urls import path
from .views import CartView
from .views import AddToCartView


app_name = 'cart'

urlpatterns = [
    path('cart/', CartView.as_view(), name='cart.html'),  
    
    
    path('add-to-cart/<int:item_id>/', AddToCartView.as_view(), name='add-to-cart'),
]
