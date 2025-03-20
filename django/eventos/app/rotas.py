from django.urls import path
from . import views

urlpatterns = [
    path('create/',views.create_evento),
    path('read/',views.read_eventos),
    path('read/<int:pk>',views.read_evento),
    path('update/<int:pk>',views.update_evento),
    path('delete/<int:pk>',views.delete_evento),
    path('patch/<int:pk>',views.update_partial_evento)
]