from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)

router.register(r'professores', views.ProfessorView)
router.register(r'reservaAmbiente', views.AmbienteView)
router.register(r'disciplina', views.DisciplinaView)


urlpatterns = [
    path('', include(router.urls)),
    path('token/', view=views.LoginView.as_view()),
    path('cadastro/', view=views.CadastroView.as_view())
]