from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
   path('user_profile',views.user_profile),
   path('u_update/<int:id>',views.u_update,name='u_update'),
   path('u_update/user_update/<int:id>',views.user_update,name='user_update'),
   path('order/<int:id>', views.order, name='order'),
   path('order/orders', views.orders, name='orders'), 
   path('make_order',views.make_order),
   path('view_myorder',views.view_myorder),
   path('orderdelete/<int:id>',views.orderdelete,name='orderdelete'),
  
]