from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('noticias/', views.noticias),
    path('post/', views.post),
    path('post/<int:id>', views.post),
    path('contacto/', views.contacto),
    path('login/', views.loginPage),
    path('logout/', views.logoutPage),
    path('registro/', views.registerPage),
    path('comentario/', views.comment)
    
]