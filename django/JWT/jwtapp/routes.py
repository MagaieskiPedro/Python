from django.urls import path
from . import views

urlpatterns = [
    path('registrar/',view=views.registrar, name='registrar'),
]