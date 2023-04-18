from django.urls import path

from . import views

app_name = "central"
urlpatterns = [
    path('', views.index, name='index'),
    path('registrohistorico/', views.mostrar_registro_historico, name='mostrar_registro_historico'),
    path('carrosdentro/', views.mostrar_carros_dentro, name='mostrar_carros_dentro')
]