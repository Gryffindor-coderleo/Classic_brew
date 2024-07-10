from django.contrib import admin
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('add_menu',views.add_menu),
    path('view_user',views.view_user),
    path('userdelete/<int:id>',views.userdelete,name='userdelete'),
    path('view_menu',views.view_menu),
    path('view_emp',views.view_emp),
    path('empdelete/<int:id>',views.empdelete,name='empdelete'),
    path('view_order',views.view_order),
    
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
