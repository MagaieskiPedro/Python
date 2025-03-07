from django.urls import path
from . import views

urlpatterns = [
    path('criar/',views.create, name='criar'),
    path('consulta/',views.read, name='consulta'),
    path('alterar/<int:pk>',views.update, name='alterar'),
    path('apagar/<int:pk>',views.delete, name='apagar'),
]