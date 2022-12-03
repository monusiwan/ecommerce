from django.urls import path
from .views import *
from .middlewares.auth import auth_middleware
urlpatterns = [
    path('check/',checkview,name='check'),
    path('',home.as_view(),name='home'),
    path('signup/',signupView,name='signup'),
    path('login/',login_view,name='login'),
    path('logout/',logout_view,name='logout'),
    path('product/',product_view,name='product'),
    path('store/',store_view,name='store'),
    path('cart/',Cart.as_view(),name='cart'),
    path('check-out',Checkout.as_view(),name='checkout'),
    path('orders/',auth_middleware(order_view),name='order'),
]