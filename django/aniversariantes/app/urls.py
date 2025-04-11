from . import views

from django.urls import path

urlpatterns = [
    path('aniversariante/', view=views.AniversarianteListCreateAPIView.as_view(), name='criar_listar'),
]