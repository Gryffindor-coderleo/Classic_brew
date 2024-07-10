from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
   path('emp_register',views.emp_register),
   path('emp_profile',views.emp_profile),
   path('e_update/<int:id>',views.e_update,name='e_update'),
   path('e_update/emp_update/<int:id>',views.emp_update,name='emp_update'),
]