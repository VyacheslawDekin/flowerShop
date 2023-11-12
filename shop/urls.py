from django.urls import path
from . import views

# /
urlpatterns = [
    path('', views.home, name='home'),
    # path('about', views.about, name='about'),
    path('category/<int:category_id>', views.home, name='category'),
    path('category/<int:category_id>/<int:product_id>', views.product, name='product'),
    path('cart', views.cart, name='cart'),
    path('cart/add/<int:product_id>', views.add_cart, name='add_cart'),
    path('cart/remove/<int:product_id>', views.cart_reduce, name='cart_reduce'),
    path('cart/remove_product/<int:product_id>', views.cart_remove_product, name='cart_remove_product'),

    path('account/login', views.login_, name='login'),
    path('account/signup', views.signup, name='signup'),
    path('account/signout', views.signout, name='signout'),
]
