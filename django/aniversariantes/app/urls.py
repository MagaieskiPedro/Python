from . import views

from django.urls import path

urlpatterns = [
    path('aniversariante/', view=views.AniversarianteListCreateAPIView.as_view(), name='criar_listar'),
    path('aniversariante/<int:pk>', view=views.AniversarianteRetrieveUpdateDestroyAPIView.as_view(), name='individual'),
    path('logar/', view=views.LoginView.as_view(), name='login')
]