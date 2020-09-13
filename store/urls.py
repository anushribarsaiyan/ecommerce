from django.urls import path
from . import views

urlpatterns =[
    path('store/',views.store,name='store'),
    path('cart/',views.cart,name='cart'),
    path('checkout/',views.checkout,name='checkout'),
    path('updateItem/',views.updateItem,name='updateItem'),
    path('process_order/',views.processOrder,name='process_order'),

    path('order_status/',views.order_status,name='order_status'),
    path('status_update/',views.status_update,name='status_update'),
    path('registerPage/',views.registerPage,name='registerPage'),
    path('loginpage/',views.loginPage,name='loginpage')

]
