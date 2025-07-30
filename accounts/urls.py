from django.http import HttpResponse
from django.urls import path
from . import views


urlpatterns =[
    path('',views.home,name="home"),
    path('register/',views.Registerpage,name="register"),
    path('login/',views.Loginpage,name="login"),
    path('logout/',views.logoutuser,name='logout'),
    path('products/',views.products, name="products"),
    path('customers/<str:pk_test>/', views.customers, name="customers"),
    path('create_order/<str:pk>/',views.createOrder, name="create_order"),
    path('update_order/<str:pk>/', views.updatOrder, name="update_order"),
    path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),
]