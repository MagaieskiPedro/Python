from django.urls import path
from . import views


urlpatterns = [
    path('login/', view=views.LoginView.as_view()),
    path('produto/', view=views.ProdutoListCreateAPIView.as_view()),
    path('usuario/', view=views.UsuarioListCreateAPIView.as_view()),
    path('usuario/<int:pk>', view=views.UsuarioRUDAPIView.as_view())
]