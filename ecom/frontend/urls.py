from django.urls import path

from .views import (
    IndexPage,CategoriesPage,
    CheckOutPage, ContactPage,
    ProductPage, ShoppingCart,
    RegisterClient,login_client,
    CartCreatorView,PostCommentView,
    CartRemoverView, Odr
    )

app_name = 'frontend'

urlpatterns = [
    path('', IndexPage.as_view(),name='index'),
    path('index/', IndexPage.as_view(),name='index'),
    path('categories/',CategoriesPage.as_view(),name='categories'),
    path('checkout/',Odr.as_view(),name='checkout'),
    path('contact/',ContactPage.as_view(),name='contact'),
    path('products/<int:pk>/',PostCommentView.as_view(),name='products'),
    path('cart/',ShoppingCart.as_view(),name='cart'),
    path('cart/<int:pk>/',CartRemoverView.as_view(),name='removeCart'),
    path('register/',RegisterClient.as_view(),name='register'),
    path('login/',login_client,name='login')
]