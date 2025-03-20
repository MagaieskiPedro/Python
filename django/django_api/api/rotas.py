from django.urls import path
from . import views

urlpatterns = [
    path('create/',views.create_pokemon, name="cria pokemon"),
    path('read/',views.read_pokemons, name='ler pokemons'),
    path('read/<int:pk>',views.read_pokemon, name='ler pokemon'),
    path('update/<int:pk>',views.update_pokemon, name='alterar pokemon'),
    path('delete/<int:pk>',views.delete_pokemon,name='deletar pokemon'),
    path('patch/<int:pk>',views.update_parcial_pokemon, name='alterar pokemon')
]