from django.urls import path
from MiniMart import views
from django.contrib import admin
from django.contrib.auth import views as auth_views





urlpatterns = [
    path('', views.home, name="home"),
    path('about/<str:id_num>/', views.about, name='about'),
    path('dashboard/', views.dashboard, name= 'dashboard' ),
    
    path('carts/', views.carts, name= 'carts' ),
    path('checkout/', views.checkout, name= 'checkout' ),

    path('register/', views.register, name= 'register'),
    path('login/', views.login, name= 'login'),
    path('logout/', views.logout, name= 'logout'),

    path('denied/', views.denied, name= 'denied'),

    path('profile/', views.profile, name= 'profile'),
    path('edit_profile/', views.edit_profile, name= 'edit_profile'),

    path('create_order/<str:pk>/', views.create_order, name= 'create_order'),
    path('delete_order/<str:pk>/', views.delete_order, name= 'delete_order'),
    path('update_order/<str:pk>/', views.update_order, name= 'update_order'),
    
    path("reset_password", auth_views.PasswordResetView.as_view(template_name = 'MiniMart/password_reset.html'), name="password_reset"),
    path('reset_password_sent', auth_views.PasswordResetDoneView.as_view(template_name = "MiniMart/reset_password_sent.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name = "MiniMart/reset.html"), name='password_reset_confirm'),
    path('reset_password_complete', auth_views.PasswordResetCompleteView.as_view(template_name = "MiniMart/reset_password_complete.html"), name='password_reset_complete'),      

]