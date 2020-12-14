from django.urls import path

from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('campañas/', views.campañas, name='campañas'),
    path('contacto/', views.contacto, name='contacto'),
    path('prueba/', views.prueba, name='prueba'),
]