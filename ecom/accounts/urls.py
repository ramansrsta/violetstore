from django.urls import path

from .views import (
    AddAdminView, HomePageView,
    login_view, AdminLogoutView, 
    AdminsList, UpdateAdmin,DeleteAdmin,
    AddProduct, ProductView, UpdateProduct,
    DeleteProduct, UpdateOder, OrderView
    )

app_name = 'accounts'

urlpatterns = [
    path('login/', login_view,name="login"),
    path('logout/', AdminLogoutView.as_view(),name="logout"),
    path('addProduct/', AddProduct.as_view(),name="addProduct"),
    path('viewOrder/', OrderView.as_view(),name="viewOrder"),
    
    path('updateOrder/<int:pk>/', UpdateOder.as_view(),name="updateOrder"),

    path('updateProduct/<int:pk>/', UpdateProduct.as_view(),name="updateProduct"),
    path('deleteProduct/<int:pk>/', DeleteProduct.as_view(),name="deleteProduct"),
    path('viewProduct/', ProductView.as_view(),name="viewProduct"),
    path('list/', AdminsList.as_view(),name="list"),
    path('register/', AddAdminView.as_view(),name="register"),
    path('update/<int:pk>/', UpdateAdmin.as_view(),name="update"),
    path('delete/<int:pk>/', DeleteAdmin.as_view(),name="delete"),
    path('homepage/', HomePageView.as_view(),name="homepage"),
]