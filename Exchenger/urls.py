from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('home/', views.home, name = 'home'),
    path('sign_up/', views.register, name = 'sign_up'),
    path('product_list_form/', views.product_list_form, name = 'product_list_form'),
    path('product_list/<id>', views.product_list, name = 'product_list'),
    path('product_details/<id>', views.product_details, name = 'product_details'),
    path('codegery_creation/', views.codegery_creation, name = 'codegery_creation'),
    path('search_box/', views.search_box, name = 'search_box'),
    path('message/', views.message, name = 'message'),
    path('notification/', views.notification, name = 'notification'),
    path('chat_box/', views.chat_box, name = 'chat_box'),
]