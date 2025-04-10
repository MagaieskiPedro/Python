from django.urls import path
from .views import *
urlpatterns = [
    path('listar/',view=listar_personagens, name="listar_personagem"),
    path('criar/',view=criar_bruxo),
    path('modificar/<int:pk>/',view=atualizar_bruxo)
]