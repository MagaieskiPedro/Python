from django.urls import path
from .views import ProfessorView,AmbienteView,DisciplinaView
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'professores/', ProfessorView, basename='professor')
router.register(r'ambientes/', AmbienteView, basename='ambiente')
router.register(r'disciplinas/', DisciplinaView, basename='disciplina')


urlpatterns = router.urls + [
    path('login/', view=views.LoginView.as_view())
]