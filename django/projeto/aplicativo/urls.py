from django.urls import path
from . import views

urlpatterns = [
    path('ola/',views.ordenar_postagens, name='postagens')
]